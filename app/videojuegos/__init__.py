from flask import Blueprint

bp_videojuegos=Blueprint(
    "bp_videojuegos",
    __name__,
    template_folder="templates"
)

from app.videojuegos import routes