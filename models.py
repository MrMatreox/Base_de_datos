from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Definir una clase que representa una tabla en la base de datos
class Clientes (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    cedula = db.Column(db.Integer, nullable=False)

# Constructor de la clase
    def __init__(self,nombre,apellido,cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula

