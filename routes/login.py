# routes/login.py
from flask import Blueprint, request, jsonify
from models.apoderado import Apoderado
from models.admin import Admin
from models.conductor import Conductor  # si existe
from werkzeug.security import check_password_hash

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    correo = data.get('correo')
    contraseña = data.get('contraseña')

    # Buscar usuario por correo en todas las posibles tablas
    user = (
        Admin.query.filter_by(correo=correo).first() or
        Apoderado.query.filter_by(correo=correo).first() or
        Conductor.query.filter_by(correo=correo).first()
    )

    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    # Si guardaste la contraseña hasheada, usa check_password_hash
    if user.contraseña == contraseña:  # cambia por check_password_hash(user.contraseña, contraseña) si usas hash
        return jsonify({
            "mensaje": "Login exitoso",
            "usuario": user.nombre,
            "tipo": user.tipo  # útil para saber qué vista mostrar (admin, apoderado, etc.)
        })
    else:
        return jsonify({"error": "Contraseña incorrecta"}), 401
