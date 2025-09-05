//validaciones
const validateNombre = (n) => n && n.trim().length >= 3;

const validateEmail = (e) => /^[^@]+@[^@]+\.[a-zA-Z]{2,3}$/.test(e);

const validateCantidad = (c) => !isNaN(c) && c > 0;

const validateFotos = () => {
  let fotos = document.querySelectorAll(".foto-input");
  // revisar que exista al menos un input con archivo seleccionado
  let seleccionadas = 0;
  fotos.forEach(f => { if (f.files.length > 0) seleccionadas++; });
  return seleccionadas >= 1 && seleccionadas <= 5;
};

const validateFecha = (fecha) => {
  const fechaInput = document.getElementById("fecha");
  if (!fecha) return false;
  let minFecha = new Date(fechaInput.min);
  let selectedFecha = new Date(fecha);
  return selectedFecha >= minFecha;
};

const validateTelefono = (t) => {
  if (!t) return true; 
  const re = /^\+\d{3}\.\d{8}$/;
  return re.test(t);
};

const validateContacto = (c) => {
  if (!c) return true; // opcional
  return c.length >= 4 && c.length <= 50;
};

const validateForm = () => {
  let form = document.forms["myForm"];
  let errores = [];

  if (!form["region"].value) errores.push("Región");
  if (!form["comuna"].value) errores.push("Comuna");
  if (!validateNombre(form["nombre"].value)) errores.push("Nombre");
  if (!validateEmail(form["email"].value)) errores.push("Email");
  if (!form["tipo"].value) errores.push("Tipo");
  if (!validateCantidad(form["cantidad"].value)) errores.push("Cantidad");
  if (!form["unidad"].value) errores.push("Unidad de edad");
  if (form["edad"].value === "" || form["edad"].value < 0) errores.push("Edad");
  if (!validateFotos()) errores.push("Fotos");
  if (!validateTelefono(form["celular"].value)) errores.push("Teléfono");

  const contactos = document.querySelectorAll("#contactos input");
  contactos.forEach((c) => {
    if (!validateContacto(c.value)) {
      errores.push(`Contacto`);
    }
  });

  let box = document.getElementById("val-box");
  let msg = document.getElementById("val-msg");
  let list = document.getElementById("val-list");

  if (errores.length > 0) {
    msg.innerText = "Los siguientes apartados son inválidos:";
    list.innerHTML = "";
    errores.forEach(e => {
      let li = document.createElement("li");
      li.textContent = e;
      list.appendChild(li);
    });
    box.hidden = false;
  } else {
    form.style.display = "none";
    msg.innerText = "¿Está seguro que desea agregar este aviso de adopción?";
    list.innerHTML = "";

    let btnOk = document.createElement("button");
    btnOk.innerText = "Sí, estoy seguro";
    btnOk.onclick = () => {
      msg.innerText = "Hemos recibido la información de adopción, muchas gracias y suerte!";
      list.innerHTML = "";
    };

    let btnBack = document.createElement("button");
    btnBack.innerText = "No, no estoy seguro, quiero volver al formulario";
    btnBack.onclick = () => { form.style.display = "block"; box.hidden = true; };

    list.appendChild(btnOk);
    list.appendChild(btnBack);
    box.hidden = false;
  }
};

