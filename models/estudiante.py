# models/estudiante.py
from database import db

class Estudiante(db.Model):
    __tablename__ = 'estudiante'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    apellido = db.Column(db.String, nullable=False)
    direccion = db.Column(db.String, nullable=False)
    id_apoderado = db.Column(db.Integer, db.ForeignKey('apoderado.id'), nullable=False)

    def __repr__(self):
        return f'<Estudiante {self.nombre} {self.apellido}>'
