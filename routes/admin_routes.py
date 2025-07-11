from flask import Blueprint, request, jsonify
from models.apoderado import Apoderado
from database import db

admin_routes = Blueprint('admin_routes', __name__)

# Crear apoderado
@admin_routes.route('/admin/apoderado', methods=['POST'])
def crear_apoderado():
    data = request.json

    # Validar campos requeridos
    campos = ['nombre', 'apellido', 'correo', 'contraseña', 'telefono']
    if not all(c in data for c in campos):
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    nuevo_apoderado = Apoderado(
        nombre=data['nombre'],
        apellido=data['apellido'],
        correo=data['correo'],
        contraseña=data['contraseña'],  # en producción deberías hashearla
        telefono=data['telefono'],
        tipo="apoderado"
    )
    db.session.add(nuevo_apoderado)
    db.session.commit()

    return jsonify({'mensaje': 'Apoderado creado correctamente', 'id': nuevo_apoderado.id}), 201

# Crear estudiante asociado a un apoderado
@admin_routes.route('/admin/apoderado/<int:id_apoderado>/estudiante', methods=['POST'])
def crear_estudiante(id_apoderado):
    from models.estudiante import Estudiante  # import aquí para evitar ciclos

    data = request.json

    campos = ['nombre', 'apellido', 'direccion']
    if not all(c in data for c in campos):
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    nuevo_estudiante = Estudiante(
        nombre=data['nombre'],
        apellido=data['apellido'],
        direccion=data['direccion'],
        id_apoderado=id_apoderado
    )
    db.session.add(nuevo_estudiante)
    db.session.commit()

    return jsonify({
        'mensaje': 'Estudiante registrado correctamente',
        'id': nuevo_estudiante.id
    }), 201


# Crear conductor
@admin_routes.route('/admin/conductor', methods=['POST'])
def crear_conductor():
    from models.conductor import Conductor  # importar aquí para evitar ciclos

    data = request.json

    campos = ['nombre', 'apellido', 'correo', 'contraseña', 'telefono', 'licencia']
    if not all(c in data for c in campos):
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    nuevo_conductor = Conductor(
        nombre=data['nombre'],
        apellido=data['apellido'],
        correo=data['correo'],
        contraseña=data['contraseña'],  # debería hashearse
        telefono=data['telefono'],
        licencia=data['licencia'],
        tipo="conductor"
    )
    db.session.add(nuevo_conductor)
    db.session.commit()

    return jsonify({'mensaje': 'Conductor creado correctamente', 'id': nuevo_conductor.id}), 201


# Crear furgón
@admin_routes.route('/admin/furgon', methods=['POST'])
def crear_furgon():
    from models.furgon import Furgon  # evitar import circular

    data = request.json

    campos = ['patente', 'modelo', 'capacidad', 'id_conductor']
    if not all(c in data for c in campos):
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    nuevo_furgon = Furgon(
        patente=data['patente'],
        modelo=data['modelo'],
        capacidad=data['capacidad'],
        id_conductor=data['id_conductor']
    )
    db.session.add(nuevo_furgon)
    db.session.commit()

    return jsonify({'mensaje': 'Furgón creado correctamente', 'id': nuevo_furgon.id}), 201


# Crear ruta
@admin_routes.route('/admin/ruta', methods=['POST'])
def crear_ruta():
    from models.ruta import Ruta

    data = request.json

    campos = ['nombre', 'id_furgon']
    if not all(c in data for c in campos):
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    nueva_ruta = Ruta(
        nombre=data['nombre'],
        id_furgon=data['id_furgon'],
        fecha=data.get('fecha')  # opcional
    )
    db.session.add(nueva_ruta)
    db.session.commit()

    return jsonify({'mensaje': 'Ruta creada correctamente', 'id': nueva_ruta.id}), 201

# Crear punto de ruta
@admin_routes.route('/admin/punto_ruta', methods=['POST'])
def crear_punto_ruta():
    from models.punto_de_ruta import PuntoRuta

    data = request.json

    campos = ['id_ruta', 'latitud', 'longitud', 'orden']
    if not all(c in data for c in campos):
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    nuevo_punto = PuntoRuta(
        id_ruta=data['id_ruta'],
        latitud=data['latitud'],
        longitud=data['longitud'],
        orden=data['orden']
    )
    db.session.add(nuevo_punto)
    db.session.commit()

    return jsonify({'mensaje': 'Punto de ruta creado correctamente', 'id': nuevo_punto.id}), 201

# Registrar ubicación en tiempo real del furgón
@admin_routes.route('/admin/ubicacion', methods=['POST'])
def registrar_ubicacion():
    from models.ubicacion_tiempo_real import UbicacionTiempoReal

    data = request.json
    campos = ['id_furgon', 'latitud', 'longitud']
    if not all(c in data for c in campos):
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    nueva_ubicacion = UbicacionTiempoReal(
        id_furgon=data['id_furgon'],
        latitud=data['latitud'],
        longitud=data['longitud']
    )
    db.session.add(nueva_ubicacion)
    db.session.commit()

    return jsonify({'mensaje': 'Ubicación registrada', 'id': nueva_ubicacion.id}), 201
