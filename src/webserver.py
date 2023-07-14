from flask import Flask, request, jsonify
from flask_cors import CORS
import supabase

from .supabase_conexion import authenticate
from .lecciones import *
from .cursos import *
from .usuarios import *
from .tablas import *


app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})


@app.route("/")
def admin():
    return "La Hechicera del Codigo"

# Routas para el POST


@app.route("/lesson", methods=["POST"])
def new_lesson():
    # Para recuperar la información que se recoge de postman (JSON)
    data = request.get_json()
    print("************* Nuevo leccion creado *****************", data)
    post_lesson(data)  # Para añadir la data de el nuevo
    return ""


@app.route("/course", methods=["POST"])
def new_course():
    # Para recuperar la información que se recoge de postman (JSON)
    data = request.get_json()
    print("************* Nuevo curso creado *****************", data)
    post_course(data)  # Para añadir la data de el nuevo
    return ""


@app.route("/user", methods=["POST"])
def new_user():
    # Para recuperar la información que se recoge de postman (JSON)
    data = request.get_json()
    print("************* Nuevo usuario creado *****************", data)
    post_user(data)  # Para añadir la data de el nuevo
    return ""


@app.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']

    # Realiza la autenticación utilizando supabase.auth.signIn() desde el servidor
    # y devuelve el resultado como respuesta al cliente
    response = authenticate(email, password)

    return jsonify(response)


@app.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')

    # Genera y envía el enlace mágico de autenticación
    response = supabase.auth.create_magic_link(email)
    if response.get('error'):
        return {'success': False, 'message': 'Error en el registro'}
    else:
        return {'success': True, 'message': 'Revise su correo para autorizar el registro'}


if __name__ == "__main__":
    app.run(debug=True)


"""
# @app.route("/lesson")  esto también funcionaría, no hace falta ponerle el método GET pero se pone para saber que método estamos utilizando.
@app.route("/lesson", methods=["GET"])
def all_lesson():
    return get_all_lesson()

# Conseguir todas la data de una ciudad en concreto que se mete por parámetros <city_id>


@app.route("/cities/<city_id>", methods=["GET"])
# La variable dinámica tiene que ir en <----------->
# @app.route("/cities/<city_id>") Esto también funcionaría sin GET porque por defecto se presupone que es GET pero al ponerlo dejamos constancia.
def cities(city_id):
    return get_weather_by(city_id)


# Crear una ciudad nueva
@app.route("/lesson", methods=["POST"])
def new_lesson():
    # Para recuperar la información que se recoge de postman (JSON)
    data = request.get_json()
    print("************* New City", data)
    post_lesson(data)  # Para añadir la data de el nuevo
    return ""


@app.route("/cities/<city_id>", methods=["PUT"])
def update_city(city_id):
    data = request.get_json()
    update_city_data(city_id, data)
    return ""


@app.route("/cities/<id>", methods=["DELETE"])  # Creamos la ruta delete
def delete_city(id):  # Creamos la función para la ruta y le pasamos el parámetro necesario que viene desde la ruta ID
    remove_city(id)  # Llamamos a la función que hemos creado para eleminar
#     # Agremamos el return sin devolver nada porque es obligatorio ponerlo.
    return ""
"""
