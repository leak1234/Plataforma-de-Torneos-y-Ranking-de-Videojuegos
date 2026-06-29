from flask import render_template,request,redirect,url_for,flash

from datetime import datetime

from app import db

from app.torneos import bp_torneos

from app.torneos.models import Torneo

from app.videojuegos.models import Videojuego



@bp_torneos.route("/")
def index():

    torneos = Torneo.query.all()

    return render_template(
        "torneos/index.html",
        torneos=torneos
    )





@bp_torneos.route("/create",methods=["GET","POST"])
def create():


    videojuegos = Videojuego.query.all()



    if request.method=="POST":


        torneo = Torneo(


            nombre=request.form.get("nombre"),


            fecha_inicio=datetime.strptime(
                request.form.get("fecha_inicio"),
                "%Y-%m-%d"
            ).date(),



            fecha_fin=datetime.strptime(
                request.form.get("fecha_fin"),
                "%Y-%m-%d"
            ).date(),



            estado=request.form.get("estado"),



            id_videojuego=request.form.get("id_videojuego")

        )



        db.session.add(torneo)


        db.session.commit()



        flash("Torneo creado correctamente","success")



        return redirect(
            url_for("bp_torneos.index")
        )




    return render_template(
        "torneos/create.html",
        videojuegos=videojuegos
    )







@bp_torneos.route("/editar/<int:id>",methods=["GET","POST"])
def editar(id):


    torneo = Torneo.query.get_or_404(id)


    videojuegos = Videojuego.query.all()



    if request.method=="POST":



        torneo.nombre = request.form.get("nombre")



        torneo.fecha_inicio = datetime.strptime(
            request.form.get("fecha_inicio"),
            "%Y-%m-%d"
        ).date()



        torneo.fecha_fin = datetime.strptime(
            request.form.get("fecha_fin"),
            "%Y-%m-%d"
        ).date()




        torneo.estado = request.form.get("estado")



        torneo.id_videojuego = request.form.get("id_videojuego")




        db.session.commit()



        flash("Torneo actualizado correctamente","success")



        return redirect(
            url_for("bp_torneos.index")
        )






    return render_template(
        "torneos/editar.html",
        torneo=torneo,
        videojuegos=videojuegos
    )









@bp_torneos.route("/eliminar/<int:id>")
def eliminar(id):


    torneo = Torneo.query.get_or_404(id)



    db.session.delete(torneo)



    db.session.commit()



    flash("Torneo eliminado","danger")



    return redirect(
        url_for("bp_torneos.index")
    )