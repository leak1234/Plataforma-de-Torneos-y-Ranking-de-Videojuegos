from flask import Blueprint
bp_torneo_equipo=Blueprint("bp_torneo_equipo",__name__,template_folder="templates")
from app.torneo_equipo import routes