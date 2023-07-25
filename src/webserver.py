from flask import Flask
from flask_cors import CORS


from .querys import *


def create_app(database):
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    @app.route('/', methods=['GET'])
    def home():
        return 'La hechicera del codigo'

    @app.route('/cursos', methods=['GET'])
    def def_get_cursos():
        return get_cursos()

    @app.route('/lecciones/<id>', methods=['GET'])
    def def_get_listado(id):
        return get_listado(id)

    @app.route('/leccion/<idleccion>', methods=['GET'])
    def def_get_leccion(idleccion):
        return get_leccion(idleccion)

    return app
