import os
from supabase import create_client, Client

# Supabase Credentials from GitHub Secrets
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def add_new_member():
    # Exactly matching your 9 fields
    data = {
        "name": "Hafiya Siddiqha",
        "aadhar_number": "123456789012", # Sample
        "father_name": "Siddiq",
        "mother_name": "Mrs. Siddiqha",
        "phone_number": "9030108465",
        "age": 27,
        "dob": "1997-01-01",           # Format: YYYY-MM-DD
        "joining_date": "2025-10-25",  # Format: YYYY-MM-DD
        "address": "Andhra Pradesh"
    }
    
    try:
        # Table name plural 'members'
        response = supabase.table("members").insert(data).execute()
        
        if response.data:
            print("MashaAllah! Hafiya, sabhi 9 fields ke saath data save ho gaya hai.")
        else:
            print("Warning: Response empty hai. Check table policies.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    add_new_member()
