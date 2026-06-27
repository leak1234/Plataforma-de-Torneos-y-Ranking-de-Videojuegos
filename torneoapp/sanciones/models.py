from torneoapp.app import db

class Sancion(db.Model):
    __tablename__= "sanciones"
    
    id = db.Column(db.Integer, primary_key=True)
    motivo = db.Column(db.String(100), nullable = False)
    tipo = db.Column(db.String(50), nullable = False)
    fecha_inicio = db.Column(db.Date,nullable=False)
    fecha_fin = db.Column(db.Date,nullable=False)
    
    def __repr__(self):
        return f"<SANCION: {self.motivo} - {self.tipo} - {self.fecha_inicio} - {self.fecha_fin}"
    
    jugador_id = db.Column(db.Integer,db.ForeignKey('jugadores.id'),nullable=False)