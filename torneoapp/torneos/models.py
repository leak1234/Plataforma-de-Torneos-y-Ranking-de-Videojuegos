from torneoapp import db

class Torneos(db.Model):
    __tablename__ = 'Torneos'
    id = db.Column(db.Integer, primary_key=True)
    nombre_torneo = db.Column(db.String(100), unique=True, nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    premio = db.Column(db.String(200), nullable=True)
    modalidad = db.Column(db.String(50), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuarios.id'), nullable=False)
    estado = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Torneos {self.nombre_torneo}>'