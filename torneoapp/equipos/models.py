from torneoapp import db

class Equipos(db.Model):
    __tablename__ = 'Equipos'
    id = db.Column(db.Integer, primary_key=True)
    nombre_equipo = db.Column(db.String(100), unique=True, nullable=False)
    logo = db.Column(db.String(200), nullable=True)
    fecha_fundacion = db.Column(db.Date, nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuarios.id'), nullable=False)
    estado = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Equipos {self.nombre_equipo} - {self.descripcion}>'