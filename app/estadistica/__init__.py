from flask import Blueprint
bp_estadistica=Blueprint("bp_estadistica",__name__,template_folder="templates")
from app.estadistica import routes