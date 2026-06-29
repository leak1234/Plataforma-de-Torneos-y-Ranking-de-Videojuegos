from flask import Blueprint

bp_usuarios=Blueprint("bp_usuarios",__name__,template_folder="templates")

from app.usuarios import routes