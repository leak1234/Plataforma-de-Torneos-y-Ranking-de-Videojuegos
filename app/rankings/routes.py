from flask import render_template

from app.rankings import bp_rankings

from app.usuarios.models import Usuario

from app.estadistica.models import Estadistica



@bp_rankings.route("/")
def index():

    jugadores=Usuario.query.filter_by(rol="jugador").all()

    ranking=[]


    for jugador in jugadores:

        stats=Estadistica.query.filter_by(id_usuario=jugador.id_usuario).all()


        kills=sum(x.kills for x in stats)

        assists=sum(x.assists for x in stats)

        puntos=(kills*2)+assists


        ranking.append({
            "jugador":jugador.usuario,
            "kills":kills,
            "assists":assists,
            "puntos":puntos
        })


    ranking=sorted(
        ranking,
        key=lambda x:x["puntos"],
        reverse=True
    )


    return render_template(
        "rankings/index.html",
        ranking=ranking
    )