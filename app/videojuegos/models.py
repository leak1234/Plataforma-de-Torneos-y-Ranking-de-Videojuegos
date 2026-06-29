from app import db

class Videojuego(db.Model):

    __tablename__="videojuegos"

    id_videojuego=db.Column(db.Integer,primary_key=True)

    nombre=db.Column(db.String(100),nullable=False)

    genero=db.Column(db.String(100),nullable=False)

    descripcion=db.Column(db.String(300))

    estado=db.Column(db.String(50),default="Activo")


    torneos=db.relationship(
        "Torneo",
        back_populates="videojuego"
    )


    def __repr__(self):

        return f"<Videojuego {self.nombre}>"