// Selector de región y comuna
document.addEventListener('DOMContentLoaded', function() {
    const regionSelect = document.getElementById('select-region');
    const comunaSelect = document.getElementById('select-comuna');
    
    if (regionSelect && comunaSelect) {
        // Cuando cambia la región
        regionSelect.addEventListener('change', function() {
            const regionId = this.value;
            
            if (regionId) {
                comunaSelect.disabled = false;
                
                comunaSelect.innerHTML = '<option value="" disabled selected>Cargando comunas...</option>';
                
                fetch(`/api/comunas/${regionId}`)
                    .then(response => response.json())
                    .then(comunas => {
                        comunaSelect.innerHTML = '<option value="" disabled selected>Seleccione su comuna</option>';
                        
                        comunas.forEach(comuna => {
                            const option = document.createElement('option');
                            option.value = comuna.id;
                            option.textContent = comuna.nombre;
                            comunaSelect.appendChild(option);
                        });
                    })
                    .catch(error => {
                        console.error('Error cargando comunas:', error);
                        comunaSelect.innerHTML = '<option value="" disabled selected>Error cargando comunas</option>';
                    });
            } else {
                comunaSelect.disabled = true;
                comunaSelect.innerHTML = '<option value="" disabled selected>Primero seleccione una región</option>';
            }
        });
    }

    // Configurar fecha mínima (3 horas desde ahora)
    const fechaInput = document.getElementById('fecha');
    if (fechaInput) {
        const now = new Date();
        now.setHours(now.getHours() + 3);
        
        const year = now.getFullYear();
        const month = String(now.getMonth() + 1).padStart(2, '0');
        const day = String(now.getDate()).padStart(2, '0');
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        
        const formatted = `${year}-${month}-${day}T${hours}:${minutes}`;
        fechaInput.value = formatted;
        fechaInput.min = formatted;
    }

    // Configurar botón para agregar fotos
    const addPhotoBtn = document.getElementById('add-photo-btn');
    if (addPhotoBtn) {
        addPhotoBtn.addEventListener('click', function() {
            const photoInputs = document.getElementById('photo-inputs');
            const currentInputs = photoInputs.querySelectorAll('.foto-input');
            
            if (currentInputs.length < 5) {
                const newInput = document.createElement('input');
                newInput.type = 'file';
                newInput.name = 'fotos';
                newInput.accept = 'image/*';
                newInput.classList.add('foto-input');
                
                photoInputs.appendChild(newInput);
                photoInputs.appendChild(document.createElement('br'));
            } else {
                alert('Máximo 5 fotos permitidas');
            }
        });
    }
});

// Funciones para agrandar y cerrar una imagen
function mostrarGrande(src) {
    document.getElementById('imgAmpliada').src = src;
    document.getElementById('fotoGrande').style.display = 'block';
}

function cerrarGrande() {
    document.getElementById('fotoGrande').style.display = 'none';
    document.getElementById('imgAmpliada').src = '';
}

// Función para ir a más información al clickear una fila del listado
document.addEventListener('DOMContentLoaded', function() {
    const tableRows = document.querySelectorAll('#tabla-adopciones tbody tr');
    tableRows.forEach(row => {
        row.addEventListener('click', function() {
            const avisoId = this.getAttribute('data-aviso-id');
            if (avisoId) {
                window.location.href = `/info/${avisoId}`;
            }
        });
    });
});