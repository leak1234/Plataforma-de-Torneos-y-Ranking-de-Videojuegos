from flask import Blueprint

bp_partida=Blueprint("bp_partida",__name__,template_folder="templates")

from app.partidas import routes