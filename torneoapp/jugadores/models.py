from torneoapp.app import db

class Jugador(db.Model):
    __tablename__= "jugadores"
    
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(100), nullable = False)
    pais = db.Column(db.String(50), nullable = False)
    ranking = db.Column(db.String,nullable=False)
    victorias = db.Column(db.Integer, nullable=False)
    derrotas = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"<JUGADOR: {self.nombre} - {self.pais} - {self.ranking} - {self.victorias} - {self.derrotas}"
    
