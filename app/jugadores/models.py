from app import db

class Jugador(db.Model):

    __tablename__="jugadores"

    id_jugador=db.Column(db.Integer,primary_key=True)

    nickname=db.Column(db.String(100))

    foto=db.Column(db.String(200))

    descripcion=db.Column(db.String(300))

    id_usuario=db.Column(db.Integer,db.ForeignKey("usuarios.id_usuario"))


    usuario=db.relationship("Usuario")


    def __repr__(self):

        return f"<Jugador {self.nickname}>"