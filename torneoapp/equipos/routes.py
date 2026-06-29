from flask import render_template, redirect, url_for, Blueprint, flash, request
from torneoapp import db
from torneoapp.equipos.models import Equipos
from datetime import datetime

bp_equipos = Blueprint('bp_equipos', __name__, template_folder='templates')

@bp_equipos.route('/')
def index():
    equipos = Equipos.query.all()
    return render_template('equipos/index.html', equipos=equipos)

@bp_equipos.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('equipos/create.html')
    elif request.method == 'POST':
        nombre_equipo = request.form['nombre_equipo']
        logo = request.form['logo']
        fecha_fundacion = request.form['fecha_fundacion']
        descripcion = request.form['descripcion']
        id_usuario = request.form['id_usuario']
        estado = request.form['estado']

        nuevo_equipo = Equipos(
            nombre_equipo=nombre_equipo,
            logo=logo,
            fecha_fundacion=fecha_fundacion,
            descripcion=descripcion,
            id_usuario=id_usuario,
            estado=estado
        )

        db.session.add(nuevo_equipo)
        db.session.commit()
        flash('Equipo creado exitosamente', 'success')
        return redirect(url_for('bp_equipos.index'))