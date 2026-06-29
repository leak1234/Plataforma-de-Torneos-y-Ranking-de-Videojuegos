from app import db

class Torneo(db.Model):

    __tablename__="torneos"

    id_torneo=db.Column(db.Integer,primary_key=True)

    nombre=db.Column(db.String(100),nullable=False)

    fecha_inicio=db.Column(db.Date)

    fecha_fin=db.Column(db.Date)

    estado=db.Column(db.String(50),default="Pendiente")

    id_videojuego=db.Column(db.Integer,db.ForeignKey("videojuegos.id_videojuego"))


    videojuego=db.relationship(
        "Videojuego",
        back_populates="torneos"
    )

    partidas=db.relationship(
        "Partida",
        back_populates="torneo"
    )

    equipos=db.relationship(
        "TorneoEquipo",
        back_populates="torneo"
    )

    resultados=db.relationship(
        "Resultado",
        back_populates="torneo"
    )

    equipos_torneo=db.relationship(
        "TorneoEquipo",
        back_populates="torneo"
    )


    def __repr__(self):
        return f"<Torneo {self.nombre}>"