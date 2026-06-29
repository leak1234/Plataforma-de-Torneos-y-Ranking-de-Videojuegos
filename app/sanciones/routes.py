from flask import render_template,request,redirect,url_for,flash
from app import db
from app.sanciones import bp_sanciones
from app.sanciones.models import Sancion
from app.usuarios.models import Usuario


@bp_sanciones.route("/")
def index():

    sanciones=Sancion.query.all()

    return render_template("sanciones/index.html",sanciones=sanciones)



@bp_sanciones.route("/create",methods=["GET","POST"])
def create():

    usuarios=Usuario.query.all()


    if request.method=="POST":

        sancion=Sancion(
            motivo=request.form.get("motivo"),
            fecha_sancion=request.form.get("fecha"),
            estado=request.form.get("estado"),
            id_usuario=request.form.get("usuario")
        )


        db.session.add(sancion)

        db.session.commit()


        flash("Sanción registrada","success")


        return redirect(url_for("bp_sanciones.index"))


    return render_template("sanciones/create.html",usuarios=usuarios)



@bp_sanciones.route("/editar/<int:id>",methods=["GET","POST"])
def editar(id):

    sancion=Sancion.query.get_or_404(id)

    usuarios=Usuario.query.all()


    if request.method=="POST":

        sancion.motivo=request.form.get("motivo")

        sancion.fecha_sancion=request.form.get("fecha")

        sancion.estado=request.form.get("estado")

        sancion.id_usuario=request.form.get("usuario")


        db.session.commit()


        flash("Sanción actualizada","success")


        return redirect(url_for("bp_sanciones.index"))


    return render_template("sanciones/edit.html",sancion=sancion,usuarios=usuarios)



@bp_sanciones.route("/eliminar/<int:id>")
def eliminar(id):

    sancion=Sancion.query.get_or_404(id)


    db.session.delete(sancion)

    db.session.commit()


    flash("Sanción eliminada","danger")


    return redirect(url_for("bp_sanciones.index"))