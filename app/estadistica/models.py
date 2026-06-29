from app import db

class Estadistica(db.Model):

    __tablename__="estadisticas"

    id_estadistica=db.Column(db.Integer,primary_key=True)

    kills=db.Column(db.Integer,default=0)

    deaths=db.Column(db.Integer,default=0)

    assists=db.Column(db.Integer,default=0)

    id_usuario=db.Column(db.Integer,db.ForeignKey("usuarios.id_usuario"))

    id_partida=db.Column(db.Integer,db.ForeignKey("partidas.id_partida"))

    jugador=db.relationship("Usuario")

    partida=db.relationship("Partida")


    def __repr__(self):
        return f"<Estadistica {self.id_estadistica}>"