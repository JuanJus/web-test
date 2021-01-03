from main import db

class registroPeso(db.Model):
    __tablename__ = "registro_peso"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    peso = db.Column(db.Float)
    cintura = db.Column(db.Float)
    ratio = db.Column(db.Float)
    fecha = db.Column(db.String)