from flask import request,render_template,redirect,url_for,Blueprint

from torneoapp.app import db
from torneoapp.estadisticas_Partido.models import Estadistica

bp_estadistica = Blueprint('bp_estadistica',__name__,template_folder='templates')

@bp_estadistica.route("/")
def index():
    estadisticas = Estadistica.query.all()
    return render_template('estadistica/index.html', estadisticas=estadisticas)

@bp_estadistica.route("/create",methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('estadistica/create.html')
    elif request.method == 'POST':
        kills = request.form.get('kills')
        deaths = request.form.get('deaths')
        assists = request.form.get('assists')
        puntos_obtenidos = request.form.get('puntos_obtenidos')
        tiempo_partida = request.form.get('tiempo_partida')
        partida_id = request.form.get('partida_id')
        jugador_id = request.form.get('jugador_id')
        
        estadistica = Estadistica(kills=kills, deaths=deaths, assists=assists, puntos_obtenidos=puntos_obtenidos, tiempo_partida=tiempo_partida, partida_id=partida_id, jugador_id=jugador_id)
        
        db.session.add(estadistica)
        db.session.commit()
        
        return redirect(url_for('bp_estadistica.index'))
    
# Editar estadistica
@bp_estadistica.route("/editar/<int:id>", methods=['GET','POST'])
def editar(id):
    estadistica = Estadistica.query.get_or_404(id)
    if request.method == 'POST':
        estadistica.kills = request.form.get('kills')
        estadistica.deaths = request.form.get('deaths')
        estadistica.assists = request.form.get('assists')
        estadistica.puntos_obtenidos = request.form.get('puntos_obtenidos')
        estadistica.tiempo_partida = request.form.get('tiempo_partida')
        estadistica.partida_id = request.form.get('partida_id')
        estadistica.jugador_id = request.form.get('jugador_id')
        db.session.commit()
        return redirect(url_for('bp_estadistica.index'))
    return render_template('estadistica/editar.html', estadistica=estadistica)

# Eliminar estadistica
@bp_estadistica.route("/eliminar/<int:id>",methods=['POST'])
def eliminar(id):
    estadistica = Estadistica.query.get_or_404(id)
    db.session.delete(estadistica)
    db.session.commit()
    return redirect(url_for('bp_estadistica.index'))