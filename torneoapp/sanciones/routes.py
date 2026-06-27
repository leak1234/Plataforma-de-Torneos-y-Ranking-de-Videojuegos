from flask import request,render_template,redirect,url_for,Blueprint

from torneoapp.app import db
from torneoapp.sanciones.models import Sancion

bp_sancion = Blueprint('bp_sancion',__name__,template_folder='templates')

@bp_sancion.route("/")
def index():
    sancions = Sancion.query.all()
    return render_template('sancion/index.html', sancions=sancions)

@bp_sancion.route("/create",methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('sancion/create.html')
    elif request.method == 'POST':
        motivo = request.form.get('motivo')
        tipo = request.form.get('tipo')
        fecha_inicio = request.form.get('fecha_inicio')
        fecha_fin = request.form.get('fecha_fin')
        jugador_id = request.form.get('jugador_id')
        sancion = Sancion(motivo=motivo, tipo=tipo,fecha_inicio=fecha_inicio,fecha_fin=fecha_fin,jugador_id=jugador_id)
        
        db.session.add(sancion)
        db.session.commit()
        
        return redirect(url_for('bp_sancion.index'))
    
# Editar sancion
@bp_sancion.route("/editar/<int:id>", methods=['GET','POST'])
def editar(id):
    sancion = Sancion.query.get_or_404(id)
    if request.method == 'POST':
        sancion.motivo = request.form.get('motivo')
        sancion.tipo = request.form.get('tipo')
        sancion.fecha_inicio = request.form.get('fecha_inicio')
        sancion.fecha_fin = request.form.get('fecha_fin')
        sancion.jugador_id = request.form.get('jugador_id')     
        db.session.commit()
        return redirect(url_for('bp_sancion.index'))
    return render_template('sancion/editar.html', sancion=sancion)

# Eliminar sancion
@bp_sancion.route("/eliminar/<int:id>",methods=['POST'])
def eliminar(id):
    sancion = Sancion.query.get_or_404(id)
    db.session.delete(sancion)
    db.session.commit()
    return redirect(url_for('bp_sancion.index'))