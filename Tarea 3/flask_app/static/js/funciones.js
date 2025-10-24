document.addEventListener("DOMContentLoaded", () => {
  const regionSelect = document.getElementById("region-select");
  const comunaSelect = document.getElementById("comuna-select");

  if (!regionSelect || !comunaSelect) return;

  comunaSelect.disabled = true;

  regionSelect.addEventListener("change", () => {
    const regionId = regionSelect.value;
    const opciones = comunaSelect.querySelectorAll("option");

    comunaSelect.disabled = false;
    comunaSelect.value = "";

    opciones.forEach(opt => {
      if (!opt.dataset.region) {
        opt.hidden = false;
        return;
      }
      opt.hidden = opt.dataset.region !== regionId;
    });

    if (!regionId) {
      comunaSelect.disabled = true;
    }
  });
})

//Funciones para agrandar y cerrar una imagen
function mostrarGrande(src) {
      document.getElementById("imgAmpliada").src = src;
      document.getElementById("fotoGrande").style.display = "block";
}
function cerrarGrande() {
    document.getElementById("fotoGrande").style.display = "none";
    document.getElementById("imgAmpliada").src = "";
}

// Fecha a partir de 3 horas de la hora actual
window.addEventListener("load", () => {
  const fechaInput = document.getElementById("fecha");
  if (fechaInput) {
    let now = new Date();
    now.setHours(now.getHours() + 3);
    fechaInput.value = now.toISOString().slice(0, 16);
    fechaInput.min = fechaInput.value;
  }
});

// Función para agregar fotos (máx 5)
document.addEventListener("DOMContentLoaded", () => {
  const addBtn = document.getElementById("add-photo-btn");
  if (addBtn) {
    addBtn.addEventListener("click", () => {
      const cont = document.getElementById("photo-inputs");
      const total = cont.querySelectorAll(".foto-input").length;
      if (total < 5) {
        const input = document.createElement("input");
        input.type = "file";
        input.name = "fotos";
        input.accept = "image/*";
        input.classList.add("foto-input");
        cont.appendChild(input);
        cont.appendChild(document.createElement("br"));
      }
    });
  }
});

// Contactos
let contadorContactos = 0;
const maxContactos = 5;

function agregarContacto() {
  const red = document.getElementById("red").value;
  const contenedor = document.getElementById("contactos");
  
  if (!red) {
    alert("Selecciona una red antes de agregar.");
    return;
  }
  if (contadorContactos >= maxContactos) {
    alert("Solo puedes agregar hasta 5 redes sociales.");
    return;
  }

  contadorContactos++;

  const div = document.createElement("div");
  div.classList.add("contacto-item");
  div.innerHTML = `
    <label>${red}:</label>
    <input type="hidden" name="red_${contadorContactos}" value="${red}">
    <input type="text" name="contacto_${contadorContactos}"  placeholder="ID o URL de ${red}" required>
    
  `;
  contenedor.appendChild(div);

  document.getElementById("red").value = "";
}

// Click en una fila
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("#tabla-adopciones tbody tr").forEach(row => {
    row.addEventListener("click", () => {
      const id = row.getAttribute("data-id");
      if (id) {
        window.location.href = `/info/${id}`;
      }
    });
  });
});