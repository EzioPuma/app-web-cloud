from flask import Flask, render_template, request
from database.db import *

app = Flask(__name__)

@app.route("/")
def home_page():
    connectionSQL()
    return render_template("home.html")
    
@app.route("/register_page")
def register_page():
    return render_template("register.html")


if __name__ == "__main__":
    host = '0.0.0.0'
    port = '8080'
    app.run(host, port)