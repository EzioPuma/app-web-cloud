from flask import Flask, render_template, request, jsonify, send_from_directory
import os

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

@app.route('/servicios')
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

if __name__ == "__main__":
    host = '0.0.0.0'
    port = '8080'
    app.run(host, port)