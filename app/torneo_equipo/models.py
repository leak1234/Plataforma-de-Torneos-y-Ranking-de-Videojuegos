from app import db

class TorneoEquipo(db.Model):

    __tablename__="torneo_equipo"

    id_torneo_equipo=db.Column(db.Integer,primary_key=True)

    id_torneo=db.Column(db.Integer,db.ForeignKey("torneos.id_torneo"))

    id_equipo=db.Column(db.Integer,db.ForeignKey("equipos.id_equipo"))


    torneo=db.relationship("Torneo",back_populates="equipos_torneo")

    equipo=db.relationship("Equipo",back_populates="torneos")


    estado=db.Column(db.String(50),default="Participando")


    def __repr__(self):

        return f"<TorneoEquipo {self.id_torneo}>"