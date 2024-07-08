from controller.control import *
from server import app

@app.route("/")
def home_page():
    return func_home_page()

@app.route("/register_page")
def register_page():
    return func_register_page()

@app.route("/consult_page")
def consult_page():
    return func_consult_page()

@app.route("/register_service", methods=["POST"])
def register_service():
    return func_register_service()

@app.route("/consult_service", methods=["POST"])
def consult_service():
    return func_consult_service()
