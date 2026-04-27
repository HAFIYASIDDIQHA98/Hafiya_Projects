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
        "age": age  # Kyuki aapki table mein age column hai, hum ye bhejenge
    }
    try:
        # 'members' table mein data insert karna
        response = supabase.table("members").insert(data).execute()
        print(f"MashaAllah! {name} ka account register ho gaya hai.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Aapka data (age 27 ke saath)
    add_new_member("Hafiya Siddiqha", "9030108465", "Andhra Pradesh", 27)
