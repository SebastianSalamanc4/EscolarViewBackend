from database import db

class Conductor(db.Model):
    __tablename__ = 'conductor'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    apellido = db.Column(db.String, nullable=False)
    correo = db.Column(db.String, unique=True, nullable=False)
    contraseña = db.Column(db.String, nullable=False)
    telefono = db.Column(db.String, nullable=False)
    tipo = db.Column(db.String, nullable=False, default='conductor')
    licencia = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Conductor {self.nombre} {self.apellido}>'
