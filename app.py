from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from database import db  # importamos SQLAlchemy ya inicializado

# Cargar variables del entorno (.env)
load_dotenv()

# Crear aplicación Flask
app = Flask(__name__)

# Configurar CORS
CORS(app, supports_credentials=True, origins=["http://localhost:3000"])

# Configurar base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

# Registrar modelos y blueprints
with app.app_context():
    from models.apoderado import Apoderado
    from models.estudiante import Estudiante
    from models.admin import Admin

    # Importar y registrar el blueprint de login
    from routes.login import login_bp
    app.register_blueprint(login_bp)

    # Prints de prueba
    print("Apoderado test:", Apoderado.query.first())
    print("Estudiante test:", Estudiante.query.first())
    print("Admin test:", Admin.query.first())

# Ruta raíz de prueba
@app.route('/')
def home():
    return 'Servidor EscolarView funcionando correctamente 🚐'

# Iniciar servidor
if __name__ == '__main__':
    app.run(debug=True, port=5000)
