from flask import render_template

from app.jugadores import bp_jugador

from app.jugadores.models import Jugador

from app.estadistica.models import Estadistica


@bp_jugador.route("/")
def index():

    jugadores=Jugador.query.all()

    return render_template("jugadores/index.html",jugadores=jugadores)



@bp_jugador.route("/perfil/<int:id>")
def perfil(id):

    jugador=Jugador.query.get_or_404(id)

    estadisticas=Estadistica.query.filter_by(id_usuario=jugador.id_usuario).all()


    kills=sum(x.kills for x in estadisticas)

    deaths=sum(x.deaths for x in estadisticas)

    assists=sum(x.assists for x in estadisticas)


    return render_template("jugadores/perfil.html",jugador=jugador,kills=kills,deaths=deaths,assists=assists)