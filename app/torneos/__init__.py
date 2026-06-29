from flask import Blueprint

bp_torneos=Blueprint(
    "bp_torneos",
    __name__,
    template_folder="templates"
)

from app.torneos import routes