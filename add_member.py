import os
from supabase import create_client, Client

# Credentials uthana
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def add_new_member(name, phone, address):
    data = {
        "name": name,
        "phone": phone,
        "address": address
    }
    try:
        # 'members' table mein data dalna
        response = supabase.table("members").insert(data).execute()
        print(f"MashaAllah! {name} ka account Al-Ameen Bank mein khul gaya hai.")
    except Exception as e:
        print(f"Database Error: {e}")

if __name__ == "__main__":
    # Test ke liye aapka naam add kar rahe hain
    add_new_member("Hafiya Siddiqha", "9030108465", "Andhra Pradesh")
