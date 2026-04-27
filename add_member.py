import os
from supabase import create_client, Client

# Credentials from GitHub Secrets
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def add_new_member():
    # Exactly matching your provided SQL: name, father_name, mobile, address
    # id and created_at will be handled by Supabase automatically
    data = {
        "name": "Hafiya Siddiqha",
        "father_name": "Siddiq", 
        "mobile": "9030108465",
        "address": "Andhra Pradesh"
    }
    
    try:
        response = supabase.table("members").insert(data).execute()
        print("MashaAllah! Record successfully save ho gaya hai.")
    except Exception as e:
        print(f"Error details: {e}")

if __name__ == "__main__":
    add_new_member()
