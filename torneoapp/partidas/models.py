from torneoapp.app import db

class Partida(db.Model):
    __tablename__= "partidas"
    
    id = db.Column(db.Integer, primary_key=True)
    ronda = db.Column(db.String, nullable = False)
    fecha = db.Column(db.Date, nullable = False)
    estado =db.Column(db.String,nullable = False)
    
    def __repr__(self):
        return f"<PARTIDA: {self.ronda} - {self.fecha} - {self.estado}"
    
    estadistica_id= db.Column(db.Integer,db.ForeignKey('estadisticas.id'),nullable=False)