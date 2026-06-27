from flask import request,render_template,redirect,url_for,Blueprint

from torneoapp.app import db
from torneoapp.torneo_equipo.models import Torneo_Equipo

bp_torneo_equipo = Blueprint('bp_torneo_equipo',__name__,template_folder='templates')

@bp_torneo_equipo.route("/")
def index():
    torneo_equipos = Torneo_Equipo.query.all()
    return render_template('torneo_equipo/index.html', torneo_equipos=torneo_equipos)

@bp_torneo_equipo.route("/create",methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('torneo_equipo/create.html')
    elif request.method == 'POST':
        fecha_inscripcion = request.form.get('fecha_inscripcion')
        #equipo_id = request.form.get('equipo_id')
        torneo_equipo = Torneo_Equipo(fecha_inscripcion=fecha_inscripcion)
        
        db.session.add(torneo_equipo)
        db.session.commit()
        
        return redirect(url_for('bp_torneo_equipo.index'))
    
# Editar torneo_equipo
@bp_torneo_equipo.route("/editar/<int:id>", methods=['GET','POST'])
def editar(id):
    torneo_equipo = Torneo_Equipo.query.get_or_404(id)
    if request.method == 'POST':
        torneo_equipo.fecha_inscripcion = request.form.get('fecha_inscripcion')
        #torneo_equipo.equipo_id = request.form.get('equipo_id')     
        db.session.commit()
        return redirect(url_for('bp_torneo_equipo.index'))
    return render_template('torneo_equipo/editar.html', torneo_equipo=torneo_equipo)

# Eliminar torneo_equipo
@bp_torneo_equipo.route("/eliminar/<int:id>",methods=['POST'])
def eliminar(id):
    torneo_equipo = Torneo_Equipo.query.get_or_404(id)
    db.session.delete(torneo_equipo)
    db.session.commit()
    return redirect(url_for('bp_torneo_equipo.index'))