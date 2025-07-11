from database import db

class PuntoDeRuta(db.Model):
    __tablename__ = 'punto_de_ruta'

    id = db.Column(db.Integer, primary_key=True)
    id_ruta = db.Column(db.Integer, db.ForeignKey('ruta.id'), nullable=False)
    latitud = db.Column(db.Float, nullable=False)
    longitud = db.Column(db.Float, nullable=False)
    orden = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<PuntoDeRuta {self.id} - Orden {self.orden}>'
