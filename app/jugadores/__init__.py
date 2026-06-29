from flask import Blueprint
bp_jugador=Blueprint("bp_jugador",__name__,template_folder="templates")
from app.jugadores import routes