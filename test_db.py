import os
from supabase import create_client, Client

# GitHub Secrets se keys uthana
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

# Database se connect karna
supabase: Client = create_client(url, key)

def check_connection():
    try:
        # Table se data mangne ki koshish (abhi khali hogi)
        response = supabase.table("members").select("*").execute()
        print("MashaAllah! Connection kamyab raha.")
        print("Aapka Digital Register (Supabase) ab Python se juda hua hai.")
    except Exception as e:
        print(f"Oops! Kuch galti hui: {e}")

if __name__ == "__main__":
    check_connection()
