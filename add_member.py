import os
from supabase import create_client, Client

# Environment variables
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def add_new_member():
    # Exactly matching your 9 fields
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
        # Inserting into 'members' table
        print("Data bhej rahe hain...")
        response = supabase.table("members").insert(data).execute()
        
        # Check if record is returned
        if response.data:
            print(f"MashaAllah! Record added successfully: {response.data}")
        else:
            print("Error: Database ne data toh liya par response nahi diya.")
            
    except Exception as e:
        print(f"Bahut badi galti: {e}")

if __name__ == "__main__":
    add_new_member()
