from app import db

class EquipoJugador(db.Model):

    __tablename__="equipo_jugadores"

    id_equipo_jugador=db.Column(db.Integer,primary_key=True)

    id_equipo=db.Column(db.Integer,db.ForeignKey("equipos.id_equipo"))

    id_usuario=db.Column(db.Integer,db.ForeignKey("usuarios.id_usuario"))

    fecha_union=db.Column(db.DateTime,server_default=db.func.now())

    rol_equipo=db.Column(db.String(50),default="Jugador")


    equipo=db.relationship(
        "Equipo",
        back_populates="jugadores"
    )


    usuario=db.relationship(
        "Usuario"
    )


    def __repr__(self):

        return f"<EquipoJugador {self.id_equipo}>"