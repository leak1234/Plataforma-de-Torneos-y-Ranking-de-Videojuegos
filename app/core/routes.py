from flask import render_template

from app.core import bp_core

from app.equipos.models import Equipo

from app.torneos.models import Torneo

from app.partidas.models import Partida

from app.rankings.models import Ranking



@bp_core.route("/")
def index():


    equipos=Equipo.query.all()


    torneos=Torneo.query.all()


    partidas=Partida.query.all()


    rankings=Ranking.query.order_by(
        Ranking.puntos.desc()
    ).limit(10).all()



    return render_template(
        "core/index.html",
        equipos=equipos,
        torneos=torneos,
        partidas=partidas,
        rankings=rankings
    )