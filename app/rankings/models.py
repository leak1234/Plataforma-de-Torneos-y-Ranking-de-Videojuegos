from app import db

class Ranking(db.Model):

    __tablename__="rankings"

    id_ranking=db.Column(db.Integer,primary_key=True)

    id_usuario=db.Column(db.Integer,db.ForeignKey("usuarios.id_usuario"))

    puntos=db.Column(db.Integer,default=0)

    victorias=db.Column(db.Integer,default=0)

    derrotas=db.Column(db.Integer,default=0)


    usuario=db.relationship("Usuario")


    def __repr__(self):
        return f"<Ranking {self.id_usuario}>"