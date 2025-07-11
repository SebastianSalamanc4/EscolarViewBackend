from database import db

class Apoderado(db.Model):
    __tablename__ = 'apoderado'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    contraseña = db.Column(db.Text, nullable=False)
    telefono = db.Column(db.String(20), nullable=True)
    tipo = db.Column(db.String(20), default='apoderado', nullable=False)

    def __repr__(self):
        return f'<Apoderado {self.nombre} {self.apellido}>'
