import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_DB_URL")
key = os.getenv("SUPABASE_API_KEY")

db: Client = create_client(url, key)