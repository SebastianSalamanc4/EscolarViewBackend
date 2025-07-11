from database import db

class Furgon(db.Model):
    __tablename__ = 'furgon'

    id = db.Column(db.Integer, primary_key=True)
    patente = db.Column(db.String, unique=True, nullable=False)
    modelo = db.Column(db.String, nullable=False)
    capacidad = db.Column(db.Integer, nullable=False)
    id_conductor = db.Column(db.Integer, db.ForeignKey('conductor.id'), nullable=False)

    def __repr__(self):
        return f'<Furgon {self.patente}>'
