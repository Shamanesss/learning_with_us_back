from supabase import create_client
import os
from dotenv import load_dotenv


def conectdb():
    # Cargar las variables de entorno desde el archivo .env
    load_dotenv()

    # Obtener la URL y la clave de Supabase de las variables de entorno
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")

    # Crear una instancia de cliente de Supabase
    supabase = create_client(url, key)

    return supabase
