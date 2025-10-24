document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("commentForm");
  const list = document.getElementById("commentList");
  if (!form) return;

  form.addEventListener("submit", async (ev) => {
    ev.preventDefault();
    const nombre = document.getElementById("c_nombre").value.trim();
    const texto = document.getElementById("c_texto").value.trim();
    if (nombre.length < 3) { alert("Nombre mínimo 3 caracteres"); return; }
    if (texto.length < 5) { alert("Comentario mínimo 5 caracteres"); return; }

    const res = await fetch(`/api/aviso/${avisoId}/comentarios`, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({nombre: nombre, texto: texto})
    });
    const data = await res.json();
    if (res.ok && data.ok) {
      const li = document.createElement("li");
      li.innerHTML = `<strong>${data.nombre}</strong> (${data.fecha}): ${data.texto}`;
      list.prepend(li);
      form.reset();
    } else {
      alert("No se pudo agregar comentario: " + (data.error || res.status));
    }
  });
});
