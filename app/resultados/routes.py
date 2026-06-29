from flask import render_template,request,redirect,url_for,flash

from app import db

from app.resultados import bp_resultados

from app.resultados.models import Resultado

from app.partidas.models import Partida

from app.torneos.models import Torneo



@bp_resultados.route("/")
def index():

    resultados=Resultado.query.all()

    return render_template(
        "resultados/index.html",
        resultados=resultados
    )



@bp_resultados.route("/create",methods=["GET","POST"])
def create():

    partidas=Partida.query.all()

    torneos=Torneo.query.all()


    if request.method=="POST":


        resultado=Resultado(

            marcador_equipo1=request.form.get("marcador_equipo1"),

            marcador_equipo2=request.form.get("marcador_equipo2"),

            ganador=request.form.get("ganador"),

            id_partida=request.form.get("id_partida"),

            id_torneo=request.form.get("id_torneo")

        )


        db.session.add(resultado)

        db.session.commit()


        flash("Resultado registrado","success")


        return redirect(
            url_for("bp_resultados.index")
        )



    return render_template(
        "resultados/create.html",
        partidas=partidas,
        torneos=torneos
    )



@bp_resultados.route("/editar/<int:id>",methods=["GET","POST"])
def editar(id):

    resultado=Resultado.query.get_or_404(id)



    if request.method=="POST":


        resultado.marcador_equipo1=request.form.get("marcador_equipo1")

        resultado.marcador_equipo2=request.form.get("marcador_equipo2")

        resultado.ganador=request.form.get("ganador")


        db.session.commit()


        flash("Resultado actualizado","success")


        return redirect(
            url_for("bp_resultados.index")
        )



    return render_template(
        "resultados/editar.html",
        resultado=resultado
    )



@bp_resultados.route("/eliminar/<int:id>")
def eliminar(id):

    resultado=Resultado.query.get_or_404(id)


    db.session.delete(resultado)


    db.session.commit()


    flash("Resultado eliminado","danger")


    return redirect(
        url_for("bp_resultados.index")
    )