from app import db

class Partida(db.Model):

    __tablename__="partidas"

    id_partida=db.Column(db.Integer,primary_key=True)

    fecha=db.Column(db.String(50),nullable=False)

    ronda=db.Column(db.String(50),nullable=False)

    estado=db.Column(db.String(50),default="Pendiente")


    id_torneo=db.Column(db.Integer,db.ForeignKey("torneos.id_torneo"))

    id_equipo1=db.Column(db.Integer,db.ForeignKey("equipos.id_equipo"))

    id_equipo2=db.Column(db.Integer,db.ForeignKey("equipos.id_equipo"))


    torneo=db.relationship("Torneo",back_populates="partidas")

    equipo1=db.relationship("Equipo",foreign_keys=[id_equipo1])

    equipo2=db.relationship("Equipo",foreign_keys=[id_equipo2])

    resultado=db.relationship("Resultado",back_populates="partida",uselist=False)


    def __repr__(self):

        return f"<PARTIDA {self.id_partida}>"