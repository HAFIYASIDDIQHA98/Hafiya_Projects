import os
from supabase import create_client, Client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def add_new_member(name, phone, address, age):
    data = {
        "name": name,
        "phone": phone,
        "address": address,
        "age": age,
        "total_savings": 0  # Default value
    }
    try:
        # id aur joining_date database khud generate karega
        response = supabase.table("members").insert(data).execute()
        print(f"MashaAllah! {name} ka account register ho gaya hai.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # 27 age aur Andhra Pradesh address ke saath aapka data
    add_new_member("Hafiya Siddiqha", "9030108465", "Andhra Pradesh", 27)
