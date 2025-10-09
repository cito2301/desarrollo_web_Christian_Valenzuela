function validateForm() {
    const nombre = document.getElementById("nombre").value.trim();
    const email = document.getElementById("email").value.trim();
    const celular = document.getElementById("celular").value.trim();
    const region = document.getElementById("select-region").value;
    const comuna = document.getElementById("select-comuna").value;
    const tipo = document.getElementById("tipo").value;
    const cantidad = document.getElementById("cantidad").value;
    const edad = document.getElementById("edad").value;
    const unidad = document.getElementById("unidad").value;
    const descripcion = document.getElementById("descripcion").value.trim();
    const fecha = document.getElementById("fecha").value;

    if (nombre.length < 3) {
        alert("El nombre debe tener al menos 3 caracteres");
        return false;
    }

    if (!email.includes("@") || !email.includes(".")) {
        alert("Debe ingresar un correo válido");
        return false;
    }

    if (celular && !celular.startsWith("+")) {
        alert("El número de celular debe tener formato internacional (+56...)");
        return false;
    }

    if (!region) {
        alert("Debe seleccionar una región");
        return false;
    }

    if (!comuna) {
        alert("Debe seleccionar una comuna");
        return false;
    }

    if (!tipo) {
        alert("Debe seleccionar el tipo de mascota");
        return false;
    }

    if (cantidad < 1) {
        alert("La cantidad debe ser al menos 1");
        return false;
    }

    if (edad < 0) {
        alert("La edad no puede ser negativa");
        return false;
    }

    if (!unidad) {
        alert("Debe seleccionar la unidad de edad");
        return false;
    }

    if (descripcion.length < 10) {
        alert("La descripción debe tener al menos 10 caracteres");
        return false;
    }

    if (!fecha) {
        alert("Debe seleccionar una fecha de entrega");
        return false;
    }

    return true;
}