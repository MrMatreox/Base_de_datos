# CRUD / CREATE -- CREAR -- READ -- MOSTRAR -- UPDATE -- ACTUALIZAR -- DELETE -- ELIMINAR
# IMPORTAR LIBRERIAS
from conexion import db, app
from models import Clientes
from flask import render_template, request, redirect, url_for

#Creamos nuestra ruta principal de nuestra pagina
@app.route('/')
def index():
    return render_template('index.html')

#Creamos la ruta para cargar los datos utilizando los metodos GET (capturar) y POST (enviar del front)
@app.route('/cargar_datos', methods = ['GET','POST'])
def cargar_datos():
    #Si el metodo es POST obtenemos los datos
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        cedula = request.form['cedula']

        #Creamos un nuevo objeto de la clase Clientes con los datos obtenidos.
        datos_clientes = Clientes(nombre, apellido, cedula)

        db.session.add(datos_clientes)#Agregamos a la sesion de la base de datos
        db.session.commit()#Realizamos la transaccion

        return render_template('cargar_datos.html')
    
    return render_template('cargar_datos.html')

@app.route('/mostrar_datos', methods = ['GET','POST'])
def mostrar_datos():
    lista_clientes = Clientes.query.all()
    
    return render_template('mostrar_datos.html', lista_clientes = lista_clientes)

@app.route('/actualizar/<int:cliente_id>', methods = ['GET','POST'])
def actualizar(cliente_id):

    #Creamos un objeto nuevo y traemos solo el ID del cliente
    cliente_actualizado = Clientes.query.get(cliente_id)

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        cedula = request.form['cedula']

        cliente_actualizado.nombre = nombre
        cliente_actualizado.apellido = apellido
        cliente_actualizado.cedula = cedula

        db.session.commit()

        return redirect(url_for('mostrar_datos'))
    
    return render_template('actualizar.html', cliente_actualizado = cliente_actualizado)

@app.route('/eliminar', methods = ['GET','POST'])
def eliminar():
    if request.method == 'POST':
        id = request.form['cliente_id']

        cliente_a_eliminar = Clientes.query.filter_by(id=id).first()

        db.session.delete(cliente_a_eliminar)
        db.session.commit()

        return redirect(url_for('mostrar_datos'))