from flask import request,render_template,redirect,url_for,Blueprint

from torneoapp.app import db
from torneoapp.videojuegos.models import Juego

bp_juego = Blueprint('bp_juego',__name__,template_folder='templates')

@bp_juego.route("/")
def index():
    juegos = Juego.query.all()
    return render_template('juego/index.html', juegos=juegos)

@bp_juego.route("/create",methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('juego/create.html')
    elif request.method == 'POST':
        nombre = request.form.get('nombre')
        genero = request.form.get('genero')
        descripcion = request.form.get('descripcion')
        
        juego = Juego(nombre=nombre, genero=genero,descripcion=descripcion)
        
        db.session.add(juego)
        db.session.commit()
        
        return redirect(url_for('bp_juego.index'))
    
# Editar juego
@bp_juego.route("/editar/<int:id>", methods=['GET','POST'])
def editar(id):
    juego = Juego.query.get_or_404(id)
    if request.method == 'POST':
        juego.nombre = request.form.get('nombre')
        juego.genero = request.form.get('genero')
        juego.descripcion = request.form.get('descripcion')
        db.session.commit()
        return redirect(url_for('bp_juego.index'))
    return render_template('juego/editar.html', juego=juego)

# Eliminar juego
@bp_juego.route("/eliminar/<int:id>",methods=['POST'])
def eliminar(id):
    juego = Juego.query.get_or_404(id)
    db.session.delete(juego)
    db.session.commit()
    return redirect(url_for('bp_juego.index'))