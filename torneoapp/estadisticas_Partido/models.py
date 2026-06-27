from torneoapp.app import db

class Estadistica(db.Model):
    __tablename__= "estadisticas"
    
    id = db.Column(db.Integer, primary_key=True)
    Kills = db.Column(db.String, nullable = False)
    deaths = db.Column(db.String, nullable = False)
    assits =db.Column(db.String,nullable = False)
    puntos_obtenidos =db.Column(db.String, nullable=False)
    tiempo_partida =db.Column(db.Time,nullable=False)
    
    def __repr__(self):
        return f"<ESTADISTICA: {self.Kills} - {self.deaths} - {self.assits} - {self.puntos_obtenidos} - {self.tiempo_partida}"
    
    partida_id = db.Column(db.Integer,db.ForeignKey('partidas.id'),nullable=False)
    jugador_id = db.Column(db.Integer,db.ForeignKey('jugadores.id'),nullable=False)