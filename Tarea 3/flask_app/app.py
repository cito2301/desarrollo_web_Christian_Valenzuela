from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import db
from util import validations
from datetime import datetime
import os, uuid, hashlib, filetype

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route("/")
def portada():
    try:
        last = db.get_last_avisos(limit=5)
    except Exception as e:
        last = []
    return render_template("Portada.html", avisos=last)


@app.route("/agregar", methods=["GET","POST"])
def agregar():
    if request.method == "GET":
        regiones = db.get_regions()
        comunas = db.get_comunas()
        return render_template("Agregar.html", regiones=regiones, comunas=comunas)
    else:
        try:
            comuna = request.form.get("comuna_id")
            sector = request.form.get("sector")
            nombre = request.form.get("nombre")
            email = request.form.get("email")
            celular = request.form.get("celular")
            tipo = request.form.get("tipo")
            cantidad = request.form.get("cantidad")
            edad = request.form.get("edad")
            unidad = request.form.get("unidad")
            fecha_entrega = request.form.get("fecha")
            descripcion = request.form.get("descripcion")

            errors = []
            if not validations.validate_nombre(nombre): errors.append("nombre")
            if not validations.validate_email(email): errors.append("email")
            if not validations.validate_celular(celular): errors.append("celular")
            if not validations.validate_tipo(tipo): errors.append("tipo")
            if not validations.validate_cantidad(cantidad): errors.append("cantidad")
            if not validations.validate_unidad(unidad): errors.append("unidad")

            if not fecha_entrega:
                errors.append("fecha")
            else:
                try:
                    fdt = datetime.strptime(fecha_entrega, "%Y-%m-%dT%H:%M")
                except ValueError:
                    errors.append("fecha_invalida")

            if errors:
                regiones = db.get_regions()
                comunas = db.get_comunas()
                return render_template("Agregar.html", regiones=regiones, comunas=comunas, errors=errors, form=request.form)

            fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            aviso_id = db.insert_aviso(fecha_ingreso, comuna, sector, nombre, email, celular, tipo, int(cantidad), int(edad or 0), unidad, fecha_entrega, descripcion)

            for key in list(request.form.keys()):
                if key.startswith("contacto_"):
                    valor = request.form.get(key)
                    parts = key.split("_", 1)
                    idx = parts[1] if len(parts) > 1 else ""
                    red = request.form.get(f"red_{idx}", "otra")
                    if valor:
                        db.insert_contactar(red, valor, aviso_id)

            files = request.files.getlist("fotos")
            for f in files:
                if f and f.filename:
                    safe_name = hashlib.sha256(f.filename.encode("utf-8")).hexdigest()
                    ext = filetype.guess(f)
                    if ext:
                        extension = ext.extension
                    else:
                        extension = f.filename.rsplit(".",1)[-1]
                    filename = f"{safe_name}_{uuid.uuid4().hex}.{extension}"
                    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    ruta = f"uploads/{filename}"
                    db.insert_foto(ruta, f.filename, aviso_id)

            return redirect(url_for('portada'))
        except Exception as e:
            regiones = db.get_regions()
            comunas = db.get_comunas()
            return render_template("Agregar.html", regiones=regiones, comunas=comunas, errors=["server"], err_msg=str(e))

@app.route("/listado")
def listado():
    page = int(request.args.get("page", 1))
    per_page = 5
    offset = (page - 1) * per_page
    avisos = db.get_avisos_paginated(per_page, offset)
    prev_url = url_for('listado', page=page-1) if page>1 else None
    next_url = url_for('listado', page=page+1) if len(avisos)==per_page else None
    return render_template("Listado.html", avisos=avisos, prev_url=prev_url, next_url=next_url, page=page)

@app.route("/aviso/<int:aviso_id>")
def info_aviso(aviso_id):
    aviso = db.get_aviso_by_id(aviso_id)
    if not aviso:
        return "Aviso no encontrado", 404
    fotos = db.get_fotos(aviso_id)
    contactos = db.get_contactos(aviso_id)
    comentarios = db.get_comments(aviso_id)
    return render_template("informacion-adopcion.html", aviso=aviso, fotos=fotos, contactos=contactos, comentarios=comentarios)

@app.route("/api/aviso/<int:aviso_id>/comentarios", methods=["POST"])
def api_add_comment(aviso_id):
    data = request.get_json() or {}
    nombre = data.get("nombre","").strip()
    texto = data.get("texto","").strip()
    if not nombre or len(nombre) < 3 or len(nombre) > 80:
        return jsonify({"ok": False, "error": "nombre inválido"}), 400
    if not texto or len(texto) < 5:
        return jsonify({"ok": False, "error": "texto inválido"}), 400
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        db.insert_comment(nombre, texto, fecha, aviso_id)
    except Exception as e:
        return jsonify({"ok": False, "error": "db_error"}), 500
    return jsonify({"ok": True, "nombre": nombre, "texto": texto, "fecha": fecha})

@app.route("/api/aviso/<int:aviso_id>/comentarios", methods=["GET"])
def api_get_comments(aviso_id):
    comments = db.get_comments(aviso_id)
    out = [{"nombre": c[0], "texto": c[1], "fecha": c[2].strftime("%Y-%m-%d %H:%M:%S") if hasattr(c[2],"strftime") else str(c[2])} for c in comments]
    return jsonify(out)

@app.route("/api/estadisticas/avisos-por-dia")
def api_avisos_por_dia():
    rows = db.stats_avisos_por_dia()
    return jsonify([[str(r[0]), int(r[1])] for r in rows])

@app.route("/api/estadisticas/avisos-por-tipo")
def api_avisos_por_tipo():
    rows = db.stats_por_tipo()
    return jsonify({ r[0]: int(r[1]) for r in rows })

@app.route("/api/estadisticas/avisos-por-mes-tipo")
def api_avisos_por_mes_tipo():
    rows = db.stats_por_mes_tipo()
    out = [{"mes": int(r[0]), "tipo": r[1], "cnt": int(r[2])} for r in rows]
    return jsonify(out)

@app.route("/estadisticas")
def estadisticas():
    return render_template("Estadísticas.html")

if __name__ == "__main__":
    app.run(debug=True)
