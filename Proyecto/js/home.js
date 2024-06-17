function enviarAccion(accion) {
    $.ajax({
        type: 'POST',
        url: '/accion',
        contentType: 'application/json',
        data: JSON.stringify({ accion: accion }),
        success: function(response) {
            // Redireccionar a la página correspondiente según la acción
            if (accion === 'Inicio') {
                window.location.href = '/';
            } else {
                window.location.href = '/' + accion.toLowerCase();
            }
        },
        error: function(error) {
            console.error('Error en la solicitud:', error);
        }
    });
}