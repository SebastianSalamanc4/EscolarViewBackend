from database import db

class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    contraseña = db.Column(db.Text, nullable=False)
    tipo = db.Column(db.String(20), default='admin', nullable=False)

    def __repr__(self):
        return f'<Admin {self.nombre} {self.apellido}>'
