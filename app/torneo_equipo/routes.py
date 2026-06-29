from flask import render_template,request,redirect,url_for,flash

from app import db

from app.torneo_equipo import bp_torneo_equipo

from app.torneo_equipo.models import TorneoEquipo

from app.torneos.models import Torneo

from app.equipos.models import Equipo



@bp_torneo_equipo.route("/")
def index():

    registros=TorneoEquipo.query.all()

    return render_template("torneo_equipo/index.html",registros=registros)



@bp_torneo_equipo.route("/create",methods=["GET","POST"])
def create():

    torneos=Torneo.query.all()

    equipos=Equipo.query.all()


    if request.method=="POST":


        registro=TorneoEquipo(

            id_torneo=request.form.get("torneo"),

            id_equipo=request.form.get("equipo"),

            estado=request.form.get("estado")

        )


        db.session.add(registro)

        db.session.commit()


        flash("Equipo agregado al torneo","success")


        return redirect(url_for("bp_torneo_equipo.index"))



    return render_template("torneo_equipo/create.html",torneos=torneos,equipos=equipos)



@bp_torneo_equipo.route("/editar/<int:id>",methods=["GET","POST"])
def editar(id):

    registro=TorneoEquipo.query.get_or_404(id)


    torneos=Torneo.query.all()

    equipos=Equipo.query.all()



    if request.method=="POST":


        registro.id_torneo=request.form.get("torneo")

        registro.id_equipo=request.form.get("equipo")

        registro.estado=request.form.get("estado")



        db.session.commit()


        flash("Registro actualizado","success")


        return redirect(url_for("bp_torneo_equipo.index"))



    return render_template("torneo_equipo/edit.html",registro=registro,torneos=torneos,equipos=equipos)



@bp_torneo_equipo.route("/eliminar/<int:id>")
def eliminar(id):

    registro=TorneoEquipo.query.get_or_404(id)


    db.session.delete(registro)

    db.session.commit()


    flash("Equipo retirado del torneo","danger")


    return redirect(url_for("bp_torneo_equipo.index"))