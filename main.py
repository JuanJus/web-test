#!/home/juan/Escritorio/web_peso/env/bin/python3

from flask import Flask,redirect, url_for, render_template,request
from forms import formaPeso
from flask_sqlalchemy import SQLAlchemy
from helpers import obtener_fecha, calcular_ratio,obtener_todos_nombres

app = Flask(__name__)
app.config["SECRET_KEY"]= "hola"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://juan:2318@localhost/web_peso_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
from models import *


@app.route("/")
def home():
    db_peso = registroPeso()
    forma_html_peso = formaPeso()
    nombres_usuarios = obtener_todos_nombres(db_peso)
    
    return render_template("home.html", formas = forma_html_peso,\
                            todos_nombres = nombres_usuarios)

@app.route("/add", methods = ["POST"])
def add():
    nombre = request.form.getlist("nombre")
    peso= request.form.getlist("peso")
    cintura = request.form.getlist("cintura")
    fecha = obtener_fecha()

    ratio_cintura_altura = calcular_ratio(nombre[0], cintura[0])
    
    point = registroPeso(nombre = nombre[0].lower(),peso = peso[0],\
                         cintura = cintura[0], ratio = ratio_cintura_altura,\
                         fecha=fecha)
    db.session.add(point)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/usuario/<nombre>")
def pagina_usuario(nombre):

    db_peso = registroPeso()
    datos_completos = db_peso.query.filter_by(nombre = nombre).all()
    nombre_usuario = nombre
    todos_nombres = obtener_todos_nombres(db_peso)
    
    return render_template("usuario.html", nombre_usuario=nombre_usuario,\
                            todos_nombres=todos_nombres, db_datos = datos_completos)



if __name__ == "__main__":
    #db.drop_all()
    db.create_all()
    app.run(debug = True)
    
