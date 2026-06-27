from torneoapp.app import db

class Torneo_Equipo(db.Model):
    __tablename__= "torneo_equipos"
    
    id = db.Column(db.Integer, primary_key=True)
    fecha_inscripcion = db.Column(db.String(50), nullable = False)
    
    def __repr__(self):
        return f"<TORNEO: {self.fecha_inscripcion} "
    
    #equipo_id = db.Columb(db.Integer,db.ForeignKey('equipos.id'),nullable=False)