from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from database.db import add_service, consult_service


app = Flask(__name__)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory(os.path.join(app.root_path, 'css'), path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(os.path.join(app.root_path, 'js'), path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory(os.path.join(app.root_path, 'images'), path)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/tienda')
def tienda():
    return render_template('shop.html')

@app.route('/servicios', methods=['GET','POST'])
def servicios():
    return render_template('services.html')

@app.route('/sobre_nosotros')
def sobre_nosotros():
    return render_template('about.html')

@app.route('/accion', methods=['POST'])
def manejar_accion():
    datos = request.get_json()
    accion = datos.get('accion')

    if accion == 'Inicio':
        mensaje = "Has presionado el botón 'Inicio'"
    elif accion == 'Tienda':
        mensaje = "Has presionado el botón 'Tienda'"
    elif accion == 'Servicios':
        mensaje = "Has presionado el botón 'Servicios'"
    elif accion == 'Sobre nosotros':
        mensaje = "Has presionado el botón 'Sobre nosotros'"
    else:
        mensaje = "Acción no reconocida"

    return jsonify({'mensaje': mensaje})
    
@app.route('/submit_formulario', methods=['POST'])
def submit_formulario():
    nombremascota = request.form['nombremascota']
    tiposervicio = request.form['tiposervicio']
    nombredueno = request.form['nombredueno']
    telefonodueno = request.form['telefonodueno']
    comentarios = request.form['comentarios']
    
    service_id = add_service(nombremascota, tiposervicio, nombredueno, telefonodueno, comentarios)
    if service_id:
        return jsonify({'message': f'Servicio agregado con el ID: {service_id}', 'service_id': service_id}), 200
    else:
        return jsonify({'message': 'Error agregando el servicio'}), 500

        
        
    
@app.route('/consultar_servicio', methods=['POST'])
def consultar_servicio():
    idservicio = request.form['idservicio']
    result_data = consult_service(idservicio)
    if result_data:
        return jsonify({
            'success': True,
            'data': {
                'nombremascota': result_data[0][1],
                'tiposervicio': result_data[0][2],
                'nombredueno': result_data[0][3],
                'telefonodueno': result_data[0][4],
                'comentarios': result_data[0][5],
            }
        }), 200
    else:
        return jsonify({'success': False, 'message': 'Servicio no encontrado'}), 404


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 80
    app.run(host, port)