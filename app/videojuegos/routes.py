from flask import render_template,request,redirect,url_for,flash

from app import db

from app.videojuegos import bp_videojuegos

from app.videojuegos.models import Videojuego



@bp_videojuegos.route("/")
def index():

    videojuegos=Videojuego.query.all()

    return render_template(
        "videojuegos/index.html",
        videojuegos=videojuegos
    )



@bp_videojuegos.route("/create",methods=["GET","POST"])
def create():


    if request.method=="POST":


        juego=Videojuego(

            nombre=request.form.get("nombre"),

            genero=request.form.get("genero"),

            descripcion=request.form.get("descripcion"),

            estado="Activo"

        )


        db.session.add(juego)

        db.session.commit()


        flash("Videojuego registrado","success")


        return redirect(
            url_for("bp_videojuegos.index")
        )



    return render_template(
        "videojuegos/create.html"
    )



@bp_videojuegos.route("/editar/<int:id>",methods=["GET","POST"])
def editar(id):


    juego=Videojuego.query.get_or_404(id)



    if request.method=="POST":


        juego.nombre=request.form.get("nombre")

        juego.genero=request.form.get("genero")

        juego.descripcion=request.form.get("descripcion")

        juego.estado=request.form.get("estado")



        db.session.commit()



        flash("Videojuego actualizado","success")


        return redirect(
            url_for("bp_videojuegos.index")
        )



    return render_template(
        "videojuegos/editar.html",
        juego=juego
    )




@bp_videojuegos.route("/eliminar/<int:id>")
def eliminar(id):


    juego=Videojuego.query.get_or_404(id)


    db.session.delete(juego)


    db.session.commit()


    flash("Videojuego eliminado","danger")


    return redirect(
        url_for("bp_videojuegos.index")
    )