from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db=SQLAlchemy()
migrate=Migrate()


def create_app():

    app=Flask(__name__,template_folder="templates")

    app.config["SECRET_KEY"]="torneo_secret"

    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///torneo.db"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False


    db.init_app(app)

    migrate.init_app(app,db)



    from app.usuarios.models import Usuario
    from app.videojuegos.models import Videojuego
    from app.equipos.models import Equipo
    from app.equipo_jugadores.models import EquipoJugador
    from app.jugadores.models import Jugador
    from app.torneos.models import Torneo
    from app.torneo_equipo.models import TorneoEquipo
    from app.partidas.models import Partida
    from app.resultados.models import Resultado
    from app.rankings.models import Ranking
    from app.estadistica.models import Estadistica
    from app.sanciones.models import Sancion



    from app.core import bp_core
    from app.usuarios import bp_usuarios
    from app.videojuegos import bp_videojuegos
    from app.equipos import bp_equipos
    from app.equipo_jugadores import bp_Equipo_De_Jugadores
    from app.jugadores import bp_jugador
    from app.torneos import bp_torneos
    from app.torneo_equipo import bp_torneo_equipo
    from app.partidas import bp_partida
    from app.resultados import bp_resultados
    from app.rankings import bp_rankings
    from app.estadistica import bp_estadistica
    from app.sanciones import bp_sanciones



    app.register_blueprint(bp_core,url_prefix="/")

    app.register_blueprint(bp_usuarios,url_prefix="/usuarios")

    app.register_blueprint(bp_videojuegos,url_prefix="/videojuegos")

    app.register_blueprint(bp_equipos,url_prefix="/equipos")

    app.register_blueprint(bp_Equipo_De_Jugadores,url_prefix="/equipo_jugadores")

    app.register_blueprint(bp_jugador,url_prefix="/jugadores")

    app.register_blueprint(bp_torneos,url_prefix="/torneos")

    app.register_blueprint(bp_torneo_equipo,url_prefix="/torneo_equipo")

    app.register_blueprint(bp_partida,url_prefix="/partidas")

    app.register_blueprint(bp_resultados,url_prefix="/resultados")

    app.register_blueprint(bp_rankings,url_prefix="/rankings")

    app.register_blueprint(bp_estadistica,url_prefix="/estadistica")

    app.register_blueprint(bp_sanciones,url_prefix="/sanciones")


    return app