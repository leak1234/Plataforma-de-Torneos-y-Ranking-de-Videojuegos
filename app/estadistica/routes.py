from flask import render_template,request,redirect,url_for,flash
from app import db
from app.estadistica import bp_estadistica
from app.estadistica.models import Estadistica
from app.usuarios.models import Usuario
from app.partidas.models import Partida


@bp_estadistica.route("/")
def index():

    estadisticas=Estadistica.query.all()

    return render_template("estadistica/index.html",estadisticas=estadisticas)



@bp_estadistica.route("/create",methods=["GET","POST"])
def create():

    jugadores=Usuario.query.filter_by(rol="jugador").all()

    partidas=Partida.query.all()


    if request.method=="POST":

        estadistica=Estadistica(
            kills=request.form.get("kills"),
            deaths=request.form.get("deaths"),
            assists=request.form.get("assists"),
            id_usuario=request.form.get("id_usuario"),
            id_partida=request.form.get("id_partida")
        )


        db.session.add(estadistica)

        db.session.commit()


        flash("Estadistica registrada","success")


        return redirect(url_for("bp_estadistica.index"))


    return render_template("estadistica/create.html",jugadores=jugadores,partidas=partidas)



@bp_estadistica.route("/editar/<int:id>",methods=["GET","POST"])
def editar(id):

    estadistica=Estadistica.query.get_or_404(id)


    if request.method=="POST":

        estadistica.kills=request.form.get("kills")

        estadistica.deaths=request.form.get("deaths")

        estadistica.assists=request.form.get("assists")


        db.session.commit()


        flash("Estadistica actualizada","success")


        return redirect(url_for("bp_estadistica.index"))


    return render_template("estadistica/editar.html",estadistica=estadistica)



@bp_estadistica.route("/eliminar/<int:id>")
def eliminar(id):

    estadistica=Estadistica.query.get_or_404(id)

    db.session.delete(estadistica)

    db.session.commit()


    flash("Estadistica eliminada","danger")


    return redirect(url_for("bp_estadistica.index"))