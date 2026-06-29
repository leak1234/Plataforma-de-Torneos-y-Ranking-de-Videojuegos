from flask import render_template,request,redirect,url_for,flash

from app import db

from app.equipo_jugadores import bp_Equipo_De_Jugadores

from app.equipo_jugadores.models import EquipoJugador

from app.equipos.models import Equipo

from app.usuarios.models import Usuario


@bp_Equipo_De_Jugadores.route("/")
def index():

    jugadores=EquipoJugador.query.all()

    return render_template(
        "equipo_jugadores/index.html",
        jugadores=jugadores
    )


@bp_Equipo_De_Jugadores.route("/create",methods=["GET","POST"])
def create():

    equipos=Equipo.query.all()

    usuarios=Usuario.query.filter_by(
        rol="jugador"
    ).all()


    if request.method=="POST":

        registro=EquipoJugador(
            id_equipo=request.form.get("id_equipo"),
            id_usuario=request.form.get("id_usuario"),
            rol_equipo=request.form.get("rol_equipo")
        )


        db.session.add(registro)

        db.session.commit()


        flash("Jugador agregado al equipo","success")


        return redirect(
            url_for("bp_Equipo_De_Jugadores.index")
        )


    return render_template(
        "equipo_jugadores/create.html",
        equipos=equipos,
        usuarios=usuarios
    )



@bp_Equipo_De_Jugadores.route("/editar/<int:id>",methods=["GET","POST"])
def editar(id):

    jugador=EquipoJugador.query.get_or_404(id)


    if request.method=="POST":

        jugador.rol_equipo=request.form.get("rol_equipo")

        db.session.commit()


        flash("Rol actualizado","success")


        return redirect(
            url_for("bp_Equipo_De_Jugadores.index")
        )


    return render_template(
        "equipo_jugadores/editar.html",
        jugador=jugador
    )



@bp_Equipo_De_Jugadores.route("/eliminar/<int:id>")
def eliminar(id):

    jugador=EquipoJugador.query.get_or_404(id)

    db.session.delete(jugador)

    db.session.commit()


    flash("Jugador eliminado del roster","danger")


    return redirect(
        url_for("bp_Equipo_De_Jugadores.index")
    )