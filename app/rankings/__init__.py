from flask import Blueprint
bp_rankings=Blueprint("bp_rankings",__name__,template_folder="templates")
from app.rankings import routes