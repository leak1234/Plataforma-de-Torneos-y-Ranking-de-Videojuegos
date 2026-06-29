from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app=Flask(__name__, template_folder="templates")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bd_torneo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    migrate.init_app(app,db)
    
    # Importancion del Blueprint
    from torneoapp.estadisticas_Partido.routes import bp_estadistica
    from torneoapp.jugadores.routes import bp_jugador
    from torneoapp.partidas.routes import bp_partida
    from torneoapp.sanciones.routes import bp_sancion
    from torneoapp.torneo_equipo.routes import bp_torneo_equipo
    from torneoapp.videojuegos.routes import bp_juego
    from torneoapp.usuarios.routes import bp_usuarios
    from torneoapp.core.routes import bp_core
    from torneoapp.torneos.routes import bp_torneos
    from torneoapp.resultados.routes import bp_resultados
    from torneoapp.equipos.routes import bp_equipos
    from torneoapp.equipo_de_jugadores.routes import bp_Equipo_De_Jugadores
    from torneoapp.rankings.routes import bp_rankings


 
    # Registrar el blueprint
    app.register_blueprint(bp_estadistica, url_prefix="/estadisticas_Partido")
    app.register_blueprint(bp_jugador, url_prefix="/jugadores")
    app.register_blueprint(bp_partida, url_prefix="/partidas")
    app.register_blueprint(bp_sancion, url_prefix="/sanciones")
    app.register_blueprint(bp_torneo_equipo, url_prefix="/torneo_equipo")
    app.register_blueprint(bp_juego, url_prefix="/videojuegos")
    app.register_blueprint(bp_usuarios, url_prefix='/usuarios')
    app.register_blueprint(bp_core, url_prefix='/')
    app.register_blueprint(bp_torneos, url_prefix='/torneos')
    app.register_blueprint(bp_resultados, url_prefix='/resultados')
    app.register_blueprint(bp_equipos, url_prefix='/equipos')
    app.register_blueprint(bp_Equipo_De_Jugadores, url_prefix='/equipo_de_jugadores')
    app.register_blueprint(bp_rankings, url_prefix='/ranking')
    
    return app

    
    