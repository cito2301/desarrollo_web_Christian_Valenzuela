def validate_aviso(data):
    errores = []

    if not data.get("region"):
        errores.append("Seleccione una región.")
    if not data.get("comuna"):
        errores.append("Seleccione una comuna.")
    if not data.get("nombre") or len(data["nombre"].strip()) < 3:
        errores.append("Nombre inválido.")
    if not data.get("email") or "@" not in data["email"]:
        errores.append("Correo inválido.")
    if data.get("celular") and not data["celular"].startswith("+"):
        errores.append("Celular debe tener formato +NNN.NNNNNNNN.")
    if not data.get("tipo"):
        errores.append("Seleccione tipo de mascota.")
    if not data.get("cantidad") or int(data["cantidad"]) <= 0:
        errores.append("Cantidad inválida.")
    if not data.get("fecha_entrega"):
        errores.append("Ingrese una fecha válida.")

    return errores
