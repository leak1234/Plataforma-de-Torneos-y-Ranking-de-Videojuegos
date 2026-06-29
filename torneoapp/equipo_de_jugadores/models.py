from torneoapp import db

class EquipoDeJugadores(db.Model):
    __tablename__ = 'EquipoDeJugadores'
    id = db.Column(db.Integer, primary_key=True)
    id_jugador = db.Column(db.Integer, db.ForeignKey('Usuarios.id'), nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_salida = db.Column(db.DateTime, nullable=True)
    rol_equipo = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<EquipoDeJugadores {self.rol_equipo} - {self.id_jugador}>'