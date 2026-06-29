from app import db

class Usuario(db.Model):
    __tablename__="usuarios"

    id_usuario=db.Column(db.Integer,primary_key=True)
    usuario=db.Column(db.String(100),nullable=False)
    correo=db.Column(db.String(120),unique=True,nullable=False)
    password=db.Column(db.String(200),nullable=False)
    rol=db.Column(db.String(50),default="usuario")
    estado=db.Column(db.String(50),default="Activo")
    fecha_registro=db.Column(db.DateTime,server_default=db.func.now())

    jugador=db.relationship("Jugador",back_populates="usuario",uselist=False)

    sanciones=db.relationship("Sancion",back_populates="usuario")

    equipos=db.relationship("Equipo",back_populates="capitan")

    def __repr__(self):
        return f"<Usuario {self.usuario}>"