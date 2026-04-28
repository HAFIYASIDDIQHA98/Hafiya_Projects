import os
from supabase import create_client, Client

# Supabase Credentials from GitHub Secrets
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def add_new_member():
    # Aapke bataye huye exact 9 fields
    data = {
        "name": "Hafiya Siddiqha",
        "aadhar_number": "123456789012",
        "father_name": "Siddiq",
        "mother_name": "Mrs. Siddiqha",
        "phone_number": "9030108465",
        "age": 27,
        "dob": "1997-01-01",
        "joining_date": "2026-04-28",
        "address": "Andhra Pradesh"
    }
    
    try:
        # Table name plural 'members'
        response = supabase.table("members").insert(data).execute()
        if response.data:
            print("MashaAllah! Data successfully save ho gaya hai.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    add_new_member()
