from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from database import db  # importamos SQLAlchemy ya inicializado

# Cargar variables del entorno (.env)
load_dotenv()

# Crear aplicación Flask
app = Flask(__name__)
CORS(app)

# Configurar base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Iniciar SQLAlchemy con app
db.init_app(app)

# Importar modelos después de inicializar db
with app.app_context():
    from models.apoderado import Apoderado
    from models.estudiante import Estudiante
    from models.admin import Admin

    apoderado_test = Apoderado.query.first()
    print("Apoderado test:", apoderado_test)

    estudiante_test = Estudiante.query.first()
    print("Estudiante test:", estudiante_test)
    
    admin_test = Admin.query.first()    
    print("admin", admin_test)

@app.route('/')
def home():
    return 'Servidor EscolarView funcionando correctamente 🚐'
# Ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)   

