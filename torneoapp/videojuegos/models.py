from torneoapp.app import db

class Juego(db.Model):
    __tablename__= "juegos"
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable = False)
    genero = db.Column(db.String(50), nullable = False)
    descripcion = db.Column(db.String,nullable=False)
    
    def __repr__(self):
        return f"<JUEGO: {self.nombre} - {self.genero} - {self.descripcion}"