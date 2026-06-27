from flask import request,render_template,redirect,url_for,Blueprint

from torneoapp.app import db
from torneoapp.jugadores.models import Jugador

bp_jugador = Blueprint('bp_jugador',__name__,template_folder='templates')

@bp_jugador.route("/")
def index():
    jugadores = Jugador.query.all()
    return render_template('jugador/index.html', jugadores=jugadores)

@bp_jugador.route("/create",methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('jugador/create.html')
    elif request.method == 'POST':
        nickname = request.form.get('nickname')
        pais = request.form.get('pais')
        ranking = request.form.get('ranking')
        victorias = request.form.get('victorias')
        derrotas = request.form.get('derrotas')
        
        jugador = Jugador(nickname=nickname, pais=pais,ranking=ranking, victorias=victorias, derrotas=derrotas)
        
        db.session.add(jugador)
        db.session.commit()
        
        return redirect(url_for('bp_jugador.index'))
    
# Editar jugador
@bp_jugador.route("/editar/<int:id>", methods=['GET','POST'])
def editar(id):
    jugador = Jugador.query.get_or_404(id)
    if request.method == 'POST':
        jugador.nickname = request.form.get('nickname')
        jugador.pais = request.form.get('pais')
        jugador.ranking = request.form.get('ranking')
        jugador.victorias = request.form.get('victorias')
        jugador.derrotas = request.form.get('derrotas')
        db.session.commit()
        return redirect(url_for('bp_jugador.index'))
    return render_template('jugador/editar.html', jugador=jugador)

# Eliminar jugador
@bp_jugador.route("/eliminar/<int:id>",methods=['POST'])
def eliminar(id):
    jugador = Jugador.query.get_or_404(id)
    db.session.delete(jugador)
    db.session.commit()
    return redirect(url_for('bp_jugador.index'))