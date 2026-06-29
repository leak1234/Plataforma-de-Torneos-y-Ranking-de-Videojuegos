from blueprintapp import db

class Resultados(db.Model):
    __tablename__ = 'Resultados'
    id = db.Column(db.Integer, primary_key=True)
    id_partido = db.Column(db.Integer, db.ForeignKey('Torneos.id'), nullable=False)
    puntaje_equipo1 = db.Column(db.Integer, nullable=False)
    puntaje_equipo2 = db.Column(db.Integer, nullable=False)
    ganador = db.Column(db.String(100), nullable=False)
    fecha_partido = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Resultados {self.id_partido} - {self.ganador}>'