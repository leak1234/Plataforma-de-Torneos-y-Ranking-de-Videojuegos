from flask import render_template, redirect, url_for, Blueprint, flash, request
from blueprintapp import db
from blueprintapp.equipo_de_jugadores.models import EquipoDeJugadores

bp_Equipo_De_Jugadores = Blueprint('bp_Equipo_De_Jugadores', __name__, template_folder='templates')

@bp_Equipo_De_Jugadores.route('/')
def index():
    equipos = EquipoDeJugadores.query.all()
    return render_template('equipo_de_jugadores/index.html', equipos=equipos)

@bp_Equipo_De_Jugadores.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('equipo_de_jugadores/create.html')
    elif request.method == 'POST':
        id_equipo = request.form['id_equipo']
        id_jugador = request.form['id_jugador']
        fecha_registro = request.form['fecha_registro']
        estado = request.form['estado']

        nuevo_equipo = EquipoDeJugadores(
            id_equipo=id_equipo,
            id_jugador=id_jugador,
            fecha_registro=fecha_registro,
            estado=estado
        )

        db.session.add(nuevo_equipo)
        db.session.commit()
        flash('Equipo de jugadores creado exitosamente', 'success')
        return redirect(url_for('bp_Equipo_De_Jugadores.index'))
  