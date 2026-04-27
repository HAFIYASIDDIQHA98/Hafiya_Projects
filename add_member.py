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
        "age": age  # Aapne table mein age rakha hai, isliye ye zaroori hai
    }
    try:
        response = supabase.table("members").insert(data).execute()
        print(f"MashaAllah! {name} ka account register ho gaya hai.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Aapki table ke columns ke hisaab se data
    add_new_member("Hafiya Siddiqha", "9030108465", "Andhra Pradesh", 27)
