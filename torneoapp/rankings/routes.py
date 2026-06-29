from flask import render_template, redirect, url_for, Blueprint, flash, request
from torneoapp import db
from torneoapp.rankings.models import Rankings

bp_rankings = Blueprint('bp_rankings', __name__, template_folder='templates')

@bp_rankings.route('/')
def index():
    rankings = Rankings.query.all()
    return render_template('rankings/index.html', rankings=rankings)

@bp_rankings.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('rankings/create.html')
    elif request.method == 'POST':
        id_jugador = request.form['id_jugador']
        posicion = request.form['posicion']
        puntos = request.form['puntos']
        victorias = request.form['victorias']
        derrotas = request.form['derrotas']
        fecha_actualizacion = request.form['fecha_actualizacion']

        nuevo_ranking = Rankings(
            id_jugador=id_jugador,
            posicion=posicion,
            puntos=puntos,
            victorias=victorias,
            derrotas=derrotas,
            fecha_actualizacion=fecha_actualizacion
        )

        db.session.add(nuevo_ranking)
        db.session.commit()
        flash('Ranking creado exitosamente', 'success')
        return redirect(url_for('bp_rankings.index'))
    
