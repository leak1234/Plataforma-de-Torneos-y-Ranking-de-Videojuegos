from flask import Blueprint

bp_Equipo_De_Jugadores=Blueprint("bp_Equipo_De_Jugadores",__name__,template_folder="templates")

from app.equipo_jugadores import routes