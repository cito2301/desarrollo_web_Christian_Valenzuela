async function evaluar(avisoId) {
  let nota = null;
  while (true) {
    let entrada = prompt("Ingrese una nota entera entre 1 y 7:");
    if (entrada === null) return; 
    entrada = entrada.trim();
    if (!/^\d+$/.test(entrada)) { alert("Ingrese un número entero."); continue; }
    let n = parseInt(entrada, 10);
    if (n < 1 || n > 7) { alert("La nota debe estar entre 1 y 7."); continue; }
    nota = n;
    break;
  }

  try {
    const res = await fetch(`/api/avisos/${avisoId}/nota`, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ nota: nota })
    });
    const data = await res.json();
    if (!res.ok || !data.ok) {
      alert("Error al enviar la nota: " + (data.error || res.status));
      return;
    }

    const notaTd = document.getElementById(`nota-${avisoId}`);
    const c = document.getElementById(`count-${avisoId}`);
    if (notaTd) notaTd.textContent = data.promedio === null ? '-' : data.promedio;
    if (c) c.textContent = data.contador && data.contador > 0 ? `(${data.contador} votos)` : '';
    alert("Nota agregada correctamente.");
  } catch (err) {
    console.error(err);
    alert("Error de red al enviar la nota.");
  }
}
