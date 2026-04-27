import os
from supabase import create_client, Client
from datetime import datetime

# Supabase Credentials
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def add_new_member():
    # Aapki SQL table ke EXACT fields: 
    # name, phone, address, age, total_savings, joining_date
    # id (SERIAL) automatically database handle karega
    data = {
        "name": "Hafiya Siddiqha",
        "phone": "9030108465",
        "address": "Andhra Pradesh",
        "age": 27,
        "total_savings": 0,
        "joining_date": datetime.now().isoformat()
    }
    
    try:
        # 'members' table mein data insert karna
        response = supabase.table("members").insert(data).execute()
        print("MashaAllah! Hafiya, aapka record sahi table aur saare fields ke saath save ho gaya hai.")
    except Exception as e:
        print(f"Abhi bhi koi issue hai: {e}")

if __name__ == "__main__":
    add_new_member()
