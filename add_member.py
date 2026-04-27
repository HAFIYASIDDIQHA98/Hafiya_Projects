import os
from supabase import create_client, Client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def add_new_member():
    # Exactly matching your table columns from image_d7a1cc.png
    data = {
        "name": "Hafiya Siddiqha",
        "phone": "9030108465",
        "address": "Andhra Pradesh",
        "age": 27,
        "total_savings": 0
    }
    try:
        response = supabase.table("members").insert(data).execute()
        print("MashaAllah! Data successfully save ho gaya hai.")
    except Exception as e:
        # Agar koi column miss ho raha hoga toh ye exact error batayega
        print(f"Error details: {e}")

if __name__ == "__main__":
    add_new_member()
