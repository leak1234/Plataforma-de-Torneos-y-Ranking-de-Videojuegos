from flask import render_template,request,redirect,url_for,flash

from app import db

from app.partidas import bp_partida

from app.partidas.models import Partida

from app.torneos.models import Torneo

from app.equipos.models import Equipo


@bp_partida.route("/")
def index():

    partidas=Partida.query.all()

    return render_template("partidas/index.html",partidas=partidas)


@bp_partida.route("/create",methods=["GET","POST"])
def create():

    torneos=Torneo.query.all()

    equipos=Equipo.query.all()


    if request.method=="POST":


        partida=Partida(

            fecha=request.form.get("fecha"),

            ronda=request.form.get("ronda"),

            estado=request.form.get("estado"),

            id_torneo=request.form.get("id_torneo"),

            id_equipo1=request.form.get("id_equipo1"),

            id_equipo2=request.form.get("id_equipo2")

        )


        db.session.add(partida)

        db.session.commit()


        flash("Partida creada","success")


        return redirect(url_for("bp_partida.index"))



    return render_template("partidas/create.html",torneos=torneos,equipos=equipos)



@bp_partida.route("/editar/<int:id>",methods=["GET","POST"])
def editar(id):

    partida=Partida.query.get_or_404(id)


    if request.method=="POST":


        partida.fecha=request.form.get("fecha")

        partida.ronda=request.form.get("ronda")

        partida.estado=request.form.get("estado")


        db.session.commit()


        flash("Partida actualizada","success")


        return redirect(url_for("bp_partida.index"))



    return render_template("partidas/editar.html",partida=partida)



@bp_partida.route("/eliminar/<int:id>")
def eliminar(id):

    partida=Partida.query.get_or_404(id)


    db.session.delete(partida)

    db.session.commit()


    flash("Partida eliminada","danger")


    return redirect(url_for("bp_partida.index"))