// Definir openModal en el ámbito global
window.openModal = function(index) {
    var modal = document.getElementById("myModal");
    modal.style.display = "block";
    var propiedades = JSON.parse(document.getElementById("propiedades-data").getAttribute("data-propiedades"));
    var propiedad = propiedades[index];
    document.getElementById("editIndex").value = index;
    document.getElementById("nombrePropiedad").value = propiedad.nombrePropiedad;
    document.getElementById("tipo").value = propiedad.tipo;
    document.getElementById("comunaUbicacion").value = propiedad.comunaUbicacion;
    document.getElementById("precio").value = propiedad.precio;
    document.getElementById("metrosCuadrados").value = propiedad.metrosCuadrados;
    document.getElementById("habitaciones").value = propiedad.habitaciones;
    document.getElementById("banos").value = propiedad.banos;
    document.getElementById("estacionamientos").value = propiedad.estacionamientos;
    document.getElementById("estado").value = propiedad.estado;
};

// Función para inicializar otros eventos
function initializeEvents() {
    var modal = document.getElementById("myModal");
    var span = document.getElementsByClassName("close")[0];

    span.onclick = function() {
        modal.style.display = "none";
    };

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
}

// Ejecutar initializeEvents cuando el DOM esté listo
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeEvents);
} else {
    initializeEvents();
}