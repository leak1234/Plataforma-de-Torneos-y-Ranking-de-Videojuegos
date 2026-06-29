from flask import render_template, redirect, url_for, Blueprint, flash, request
from torneoapp import db
from torneoapp.usuarios.models import Usuarios
import datetime

bp_usuarios = Blueprint('bp_usuarios', __name__, template_folder='templates')

@bp_usuarios.route('/')
def index():
    usuarios = Usuarios.query.all()
    return render_template('usuarios/index.html', usuarios=usuarios)

@bp_usuarios.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('usuarios/create.html')
    elif request.method == 'POST':
        nombre_usuario = request.form['nombre_usuario']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        contraseña = request.form['contraseña']
        rol = request.form['rol']
        fecha_registro = datetime.datetime.now().date()
        estado = request.form['estado']

        usuario = Usuarios(
            nombre_usuario=nombre_usuario,
            nombre=nombre,
            apellido=apellido,
            email=email,
            contraseña=contraseña,
            rol=rol,
            fecha_registro=fecha_registro,
            estado=estado
        )




        db.session.add(usuario)
        db.session.commit()

        return redirect(url_for('bp_usuarios.index'))
