from flask import Flask, render_template, request, redirect, url_for, jsonify
from database.db import get_all_avisos, create_aviso, get_regions, get_comunas_by_region, get_all_comunas
from util.validations import validate_aviso
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def portada():
    avisos = get_all_avisos(limit=5)
    return render_template("Portada.html", avisos=avisos)

@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        data = {
            "region": request.form.get("region"),
            "comuna": request.form.get("comuna"),
            "sector": request.form.get("sector"),
            "nombre": request.form.get("nombre"),
            "email": request.form.get("email"),
            "celular": request.form.get("celular"),
            "tipo": request.form.get("tipo"),
            "cantidad": request.form.get("cantidad"),
            "edad": request.form.get("edad"),
            "unidad": request.form.get("unidad"),
            "descripcion": request.form.get("descripcion"),
            "fecha_entrega": datetime.strptime(request.form.get("fecha"), "%Y-%m-%dT%H:%M")
        }

        errores = validate_aviso(data)
        if errores:
            regiones = get_regions()
            comunas = get_all_comunas()
            return render_template("Agregar.html", regiones=regiones, comunas=comunas, errores=errores)

        create_aviso(**data)
        return redirect(url_for("portada"))
    
    # GET request - mostrar formulario
    regiones = get_regions()
    comunas = get_all_comunas()
    return render_template("Agregar.html", regiones=regiones, comunas=comunas)

@app.route("/listado")
def listado():
    avisos = get_all_avisos()
    return render_template("Listado.html", avisos=avisos)

@app.route("/estadisticas")
def estadisticas():
    return render_template("Estadísticas.html")

@app.route("/info/<int:id>")
def info(id):
    avisos = get_all_avisos()
    aviso = next((a for a in avisos if a.id == id), None)
    return render_template("informacion-adopcion.html", aviso=aviso)

@app.route("/api/comunas/<int:region_id>")
def api_comunas(region_id):
    comunas = get_comunas_by_region(region_id)
    return jsonify([{"id": c[0], "nombre": c[1]} for c in comunas])

if __name__ == "__main__":
    app.run(debug=True)