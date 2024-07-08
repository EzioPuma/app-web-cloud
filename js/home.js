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

$(document).ready(function() {
            $('#serviceForm').submit(function(event) {
                event.preventDefault();
                var formData = $(this).serialize();

                $.ajax({
                    type: 'POST',
                    url: '/submit_formulario',
                    data: formData,
                    success: function(response) {
                        $('#message').html('<p>' + response.message + '</p>');
                    },
                    error: function(error) {
                        $('#message').html('<p>Error al enviar el formulario</p>');
                    }
                });
            });
        });


$(document).ready(function() {
            $('#consultForm').submit(function(event) {
                event.preventDefault();
                var idServicio = $('#id_servicio').val();

                $.ajax({
                    type: 'POST',
                    url: '/consultar_servicio',
                    data: { idservicio: idServicio },
                    success: function(response) {
                        if (response.success) {
                            var data = response.data;
                            var messageHtml = '<p><strong>Nombre de la Mascota:</strong> ' + data.nombremascota + '</p>' +
                                              '<p><strong>Tipo de Servicio:</strong> ' + data.tiposervicio + '</p>' +
                                              '<p><strong>Nombre del Dueño:</strong> ' + data.nombredueno + '</p>' +
                                              '<p><strong>Teléfono de Contacto:</strong> ' + data.telefonodueno + '</p>' +
                                              '<p><strong>Comentarios:</strong> ' + data.comentarios + '</p>';
                            $('#message').html(messageHtml);
                        } else {
                            $('#message').html('<p>' + response.message + '</p>');
                        }
                    },
                    error: function(error) {
                        $('#message').html('<p>Error en la consulta</p>');
                    }
                });
            });
        });
