from app import db

class Sancion(db.Model):

    __tablename__="sanciones"

    id_sancion=db.Column(db.Integer,primary_key=True)

    motivo=db.Column(db.String(200),nullable=False)

    fecha_sancion=db.Column(db.String(50))

    estado=db.Column(db.String(50),default="Activa")

    id_usuario=db.Column(db.Integer,db.ForeignKey("usuarios.id_usuario"))

    usuario=db.relationship("Usuario",back_populates="sanciones")


    def __repr__(self):

        return f"<Sancion {self.motivo}>"