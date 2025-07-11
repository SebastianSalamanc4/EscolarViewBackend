from database import db

class Ruta(db.Model):
    __tablename__ = 'ruta'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    id_furgon = db.Column(db.Integer, db.ForeignKey('furgon.id'), nullable=False)
    fecha = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f'<Ruta {self.nombre}>'
