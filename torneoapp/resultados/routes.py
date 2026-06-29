from flask import render_template, redirect, url_for, Blueprint, flash, request
from torneoapp import db
from torneoapp.resultados.models import Resultados

bp_resultados = Blueprint('bp_resultados', __name__, template_folder='templates')

@bp_resultados.route('/')
def index():
    resultados = Resultados.query.all()
    return render_template('resultados/index.html', resultados=resultados)

@bp_resultados.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('resultados/create.html')
    elif request.method == 'POST':
        nombre_resultado = request.form['nombre_resultado']
        descripcion = request.form['descripcion']
        fecha = request.form['fecha']
        torneo_id = request.form['torneo_id']
        jugador_id = request.form['jugador_id']
        fecha_registro = request.form['fecha_registro']
        estado = request.form['estado']

        nuevo_resultado = Resultados(
            nombre_resultado=nombre_resultado,
            descripcion=descripcion,
            fecha=fecha,
            torneo_id=torneo_id,
            jugador_id=jugador_id,
            fecha_registro=fecha_registro,
            estado=estado
        )

        db.session.add(nuevo_resultado)
        db.session.commit()
        flash('Resultado creado exitosamente', 'success')
        return redirect(url_for('bp_resultados.index'))