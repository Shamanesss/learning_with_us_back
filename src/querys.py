
from dotenv import load_dotenv

import supabase
from flask import jsonify
import os
from supabase import create_client
load_dotenv()


# Obtener la URL y la clave de Supabase de las variables de entorno
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

# Crear una instancia de cliente de Supabase
supabase = create_client(url, key)


def get_cursos():
    response = supabase.table('cursos').select('*').execute()
    data = response[data]
    return jsonify(data), 200
