from flask import request,render_template,redirect,url_for,Blueprint

from torneoapp.app import db
from torneoapp.partidas.models import Partida

bp_partida = Blueprint('bp_partida',__name__,template_folder='templates')

@bp_partida.route("/")
def index():
    partidas = Partida.query.all()
    return render_template('partida/index.html', partidas=partidas)

@bp_partida.route("/create",methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('partida/create.html')
    elif request.method == 'POST':
        ronda = request.form.get('ronda')
        fecha = request.form.get('fecha')
        estado = request.form.get('estado')
        
        partida = Partida(ronda=ronda, fecha=fecha, estado=estado,)
        
        db.session.add(partida)
        db.session.commit()
        
        return redirect(url_for('bp_partida.index'))
    
# Editar partida
@bp_partida.route("/editar/<int:id>", methods=['GET','POST'])
def editar(id):
    partida = Partida.query.get_or_404(id)
    if request.method == 'POST':
        partida.ronda = request.form.get('ronda')
        partida.fecha = request.form.get('fecha')
        partida.estado = request.form.get('estado')
        db.session.commit()
        return redirect(url_for('bp_partida.index'))
    return render_template('partida/editar.html', partida=partida)

# Eliminar partida
@bp_partida.route("/eliminar/<int:id>",methods=['POST'])
def eliminar(id):
    partida = Partida.query.get_or_404(id)
    db.session.delete(partida)
    db.session.commit()
    return redirect(url_for('bp_partida.index'))