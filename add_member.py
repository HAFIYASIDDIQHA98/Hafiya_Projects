import os
from supabase import create_client, Client

# Supabase Credentials
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def add_new_member():
    # EXACT Table Name: 'members'
    # EXACT Column Names matching your SQL
    data = {
        "name": "Hafiya Siddiqha",
        "phone": "9030108465",
        "joining_date": datetime.now().isoformat(),   
        "address": "Andhra Pradesh",
        "total_savings": 0
    }
    
    try:
        # Inserting into 'members' table
        response = supabase.table("members").insert(data).execute()
        
        if response.data:
            print(f"MashaAllah! {data['name']} ka record save ho gaya hai.")
        else:
            print("Warning: Code chala par response empty hai.")
            
    except Exception as e:
        print(f"Galti hui: {e}")

if __name__ == "__main__":
    add_new_member()
