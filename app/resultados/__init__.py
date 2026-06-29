from flask import Blueprint

bp_resultados=Blueprint("bp_resultados",__name__,template_folder="templates")

from app.resultados import routes