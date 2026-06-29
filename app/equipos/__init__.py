from flask import Blueprint

bp_equipos=Blueprint("bp_equipos",__name__,template_folder="templates")

from app.equipos import routes