from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField

class formaPeso(FlaskForm):
    nombre = StringField("nombre")
    peso = FloatField("peso")
    cintura = FloatField("cintura")
    submit = SubmitField("enviar")
    
