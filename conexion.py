from flask import Flask
from models import db

#Se crea una instancia de la aplicacion flask
app = Flask(__name__)

#Se configura la URL de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clientes_registrados.db"

#Inicializamos la extension SQLAlchemy en la aplicacion Flask
db.init_app(app)

#Con esto se asegura que las operaciones con la base de datos se realicen correctamente
with app.app_context():
    db.create_all()