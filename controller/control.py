from flask import render_template, request, jsonify
from database.db import *
from controller.admin_s3 import *

def func_home_page():
    return render_template("home.html")

def func_register_page():
    return render_template("register.html")

def func_consult_page():
    return render_template("consult.html")

def func_register_service():
    nombremascota = request.form["nombremascota"]
    tiposervicio = request.form["tiposervicio"]
    nombredueno = request.form["nombredueno"]
    telefonodueno = request.form["telefonodueno"]
    comentarios = request.form["comentarios"]
    confirm_service = add_service(nombremascota, tiposervicio, nombredueno, telefonodueno, comentarios)

    # Si necesitas guardar algún archivo relacionado con el servicio en S3
    if 'photo' in request.files:
        photo = request.files["photo"]
        connection_s3()
        save_file(photo)
    
    if confirm_service:
        return "<h1>El servicio fue registrado exitosamente</h1>"
    else:
        return "<h1>Error: El servicio no fue registrado</h1>"

def func_consult_service():
    obj_service = request.get_json()
    idservicio = obj_service["idservicio"]
    result_data = consult_service(idservicio)
    
    if result_data != False and len(result_data) != 0:
        response = {
            'status': "ok",
            'nombremascota': result_data[0][1],
            'tiposervicio': result_data[0][2],
            'nombredueno': result_data[0][3],
            'telefonodueno': result_data[0][4],
            'comentarios': result_data[0][5]
        }
    else:
        response = {
            'status':"error"
        }
    
    return jsonify(response)

    