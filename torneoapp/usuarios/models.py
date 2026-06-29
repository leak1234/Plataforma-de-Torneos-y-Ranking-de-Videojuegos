from blueprintapp import db

class Usuarios(db.Model):
    __tablename__ = 'Usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(50), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contraseña = db.Column(db.String(128), nullable=False)
    rol = db.Column(db.String(20), nullable=False)
    fecha_registro = db.Column(db.DateTime, nullable=False)
    estado = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Usuarios {self.nombre} - {self.email}>'