from app import db

class Resultado(db.Model):

    __tablename__="resultados"

    id_resultado=db.Column(db.Integer,primary_key=True)

    marcador_equipo1=db.Column(db.Integer,default=0)

    marcador_equipo2=db.Column(db.Integer,default=0)

    ganador=db.Column(db.String(100))

    fecha_registro=db.Column(db.DateTime,server_default=db.func.now())


    id_partida=db.Column(
        db.Integer,
        db.ForeignKey("partidas.id_partida")
    )


    id_torneo=db.Column(
        db.Integer,
        db.ForeignKey("torneos.id_torneo")
    )


    partida=db.relationship(
        "Partida",
        back_populates="resultado"
    )


    torneo=db.relationship(
        "Torneo",
        back_populates="resultados"
    )


    def __repr__(self):

        return f"<Resultado {self.id_resultado}>"