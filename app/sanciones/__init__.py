from flask import Blueprint
bp_sanciones=Blueprint("bp_sanciones",__name__,template_folder="templates")
from app.sanciones import routes