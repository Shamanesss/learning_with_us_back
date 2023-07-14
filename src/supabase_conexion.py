from supabase import create_client, Client
import os
from dotenv import load_dotenv
load_dotenv()


def authenticate(email, password):
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    supabase = create_client(url, key)

    response = supabase.auth.sign_in(email=email, password=password)

    return response
