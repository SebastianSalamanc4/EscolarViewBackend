from database import db

class UbicacionTiempoReal(db.Model):
    __tablename__ = 'ubicacion_tiempo_real'

    id = db.Column(db.Integer, primary_key=True)
    id_furgon = db.Column(db.Integer, db.ForeignKey('furgon.id'), nullable=False)
    latitud = db.Column(db.Float, nullable=False)
    longitud = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<UbicacionTiempoReal Furgon {self.id_furgon}>'
