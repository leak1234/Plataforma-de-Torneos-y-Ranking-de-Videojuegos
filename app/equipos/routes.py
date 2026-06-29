from flask import render_template,request,redirect,url_for,flash

import random

import string

from app import db

from app.equipos import bp_equipos

from app.equipos.models import Equipo

from app.usuarios.models import Usuario



@bp_equipos.route("/")
def index():

    equipos=Equipo.query.all()

    return render_template(
        "equipos/index.html",
        equipos=equipos
    )



@bp_equipos.route("/create",methods=["GET","POST"])
def create():

    capitanes=Usuario.query.filter_by(
        rol="jugador"
    ).all()


    if request.method=="POST":


        codigo="TEAM-"+''.join(
            random.choices(
                string.ascii_uppercase+string.digits,
                k=5
            )
        )


        equipo=Equipo(

            nombre=request.form.get("nombre"),

            logo=request.form.get("logo"),

            codigo_equipo=codigo,

            id_capitan=request.form.get("id_capitan")

        )


        db.session.add(equipo)

        db.session.commit()


        flash("Equipo creado con código: "+codigo,"success")


        return redirect(
            url_for("bp_equipos.index")
        )



    return render_template(
        "equipos/create.html",
        capitanes=capitanes
    )




@bp_equipos.route("/editar/<int:id>",methods=["GET","POST"])
def editar(id):

    equipo=Equipo.query.get_or_404(id)


    if request.method=="POST":


        equipo.nombre=request.form.get("nombre")

        equipo.logo=request.form.get("logo")

        equipo.estado=request.form.get("estado")


        db.session.commit()


        flash("Equipo actualizado","success")


        return redirect(
            url_for("bp_equipos.index")
        )



    return render_template(
        "equipos/editar.html",
        equipo=equipo
    )




@bp_equipos.route("/eliminar/<int:id>")
def eliminar(id):

    equipo=Equipo.query.get_or_404(id)


    db.session.delete(equipo)

    db.session.commit()


    flash("Equipo eliminado","danger")


    return redirect(
        url_for("bp_equipos.index")
    )