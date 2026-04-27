import os
from supabase import create_client, Client

# Database credentials
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def add_new_member(name, phone, address, age, savings=0):
    """
    Al-Ameen Bank: Naye member ko register karne ka function.
    id aur joining_date database khud handle karega.
    """
    data = {
        "name": name,
        "phone": phone,
        "address": address,
        "age": age,
        "total_savings": savings
    }
    
    try:
        # 'members' table mein data insert karna
        response = supabase.table("members").insert(data).execute()
        print(f"MashaAllah! {name} ka record Al-Ameen Bank mein save ho gaya hai.")
    except Exception as e:
        print(f"Database Error: {e}")

if __name__ == "__main__":
    # Aapka data saare columns ke saath
    add_new_member(
        name="Hafiya Siddiqha", 
        phone="9030122003", 
        address="Andhra Pradesh", 
        age=26, 
        savings=0
    )
