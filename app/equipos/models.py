from app import db


class Equipo(db.Model):

    __tablename__="equipos"


    id_equipo=db.Column(db.Integer,primary_key=True)

    nombre=db.Column(db.String(100),nullable=False)

    logo=db.Column(db.String(200))

    codigo_equipo=db.Column(db.String(50),unique=True)

    estado=db.Column(db.String(50),default="Activo")


    id_capitan=db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id_usuario")
    )


    capitan=db.relationship(
        "Usuario",
        back_populates="equipos"
    )


    jugadores=db.relationship(
        "EquipoJugador",
        back_populates="equipo"
    )


    torneos=db.relationship(
        "TorneoEquipo",
        back_populates="equipo"
    )

    torneos=db.relationship(
        "TorneoEquipo",
        back_populates="equipo"
    )


    def __repr__(self):

        return f"<Equipo {self.nombre}>"