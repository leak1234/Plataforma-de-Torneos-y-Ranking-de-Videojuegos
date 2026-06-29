from flask import render_template, redirect, url_for, Blueprint, flash, request
from blueprintapp import db
from blueprintapp.torneos.models import Torneos

bp_torneos = Blueprint('bp_torneos', __name__, template_folder='templates')

@bp_torneos.route('/')
def index():
    torneos = Torneos.query.all()
    return render_template('torneos/index.html', torneos=torneos)

@bp_torneos.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('torneos/create.html')
    elif request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        fecha_inicio = request.form['fecha_inicio']
        fecha_fin = request.form['fecha_fin']
        premio = request.form['premio']
        modalidad = request.form['modalidad']
        estado = request.form['estado']

        nuevo_torneo = Torneos(
            nombre_torneo=nombre,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            premio=premio,
            modalidad=modalidad,
            estado=estado
        )

        db.session.add(nuevo_torneo)
        db.session.commit()
        flash('Torneo creado exitosamente', 'success')
        return redirect(url_for('bp_torneos.index'))