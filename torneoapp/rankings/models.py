from torneoapp import db

class Rankings(db.Model):
    __tablename__ = 'Rankings'
    id = db.Column(db.Integer, primary_key=True)
    id_jugador = db.Column(db.Integer, db.ForeignKey('Usuarios.id'), nullable=False)
    posicion = db.Column(db.Integer, nullable=False)
    puntos = db.Column(db.Integer, nullable=False)
    victorias = db.Column(db.Integer, nullable=False)
    derrotas = db.Column(db.Integer, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Rankings {self.id_jugador} - {self.posicion}>'