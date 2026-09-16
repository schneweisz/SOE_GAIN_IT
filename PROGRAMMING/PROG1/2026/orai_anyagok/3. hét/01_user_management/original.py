"""
01 - FELHASZNÁLÓ KEZELÉS
PROBLÉMA: Ez a függvény túl sok dolgot csinál egyszerre!
"""

import re
import json

users_db = [] # Globális állapot!
email_log = [] # Globális állapot!

def register_user():
    """
    EZ EGY ROSSZ FÜGGVÉNY!
    - Bemenetet kezel (input)
    - Validál
    - Adatbázisba ment (globális változó)
    - Email-t "küld" (print)
    - Összetett üzleti logika
    - Több felelősség
    """
    print("=== Felhasználó regisztráció ===")
    
    # Email bekérése és validálása
    while True:
        email = input("Email cím: ")
        if "@" not in email or "." not in email.split("@")[1]:
            print(" Hibás email formátum!")
            continue
        
        # Ellenőrzi, hogy már létezik-e
        exists = False
        for user in users_db:
            if user["email"] == email:
                exists = True
                break
        
        if exists:
            print(" Ez az email már regisztrálva van!")
            continue
        
        break
    
    # Jelszó bekérése és validálása
    while True:
        password = input("Jelszó (min 8 karakter, kell szám és betű): ")
        
        if len(password) < 8:
            print(" A jelszó túl rövid!")
            continue
        
        has_digit = False
        has_letter = False
        for char in password:
            if char.isdigit():
                has_digit = True
            if char.isalpha():
                has_letter = True
        
        if not has_digit or not has_letter:
            print(" A jelszónak tartalmaznia kell számot és betűt!")
            continue
        
        break
    
    # Név bekérése
    while True:
        name = input("Teljes név: ")
        if len(name) < 2:
            print(" A név túl rövid!")
            continue
        break
    
    # Kor bekérése és validálása
    while True:
        try:
            age = int(input("Életkor: "))
            if age < 18:
                print(" 18 év alattiak nem regisztrálhatnak!")
                continue
            if age > 120:
                print(" Irreális életkor!")
                continue
            break
        except ValueError:
            print(" Számot adj meg!")
    
    # Felhasználó kategória meghatározása
    if age < 25:
        category = "fiatal"
        discount = 0.1
    elif age < 65:
        category = "felnőtt"
        discount = 0.0
    else:
        category = "nyugdíjas"
        discount = 0.15
    
    # Felhasználói objektum létrehozása
    user = {
        "email": email,
        "password": password, # ROSSZ GYAKORLAT: tiszta szövegben!
        "name": name,
        "age": age,
        "category": category,
        "discount": discount,
        "registration_date": "2026-02-24", # Hardcoded!
        "active": True
    }
    
    # Mentés az "adatbázisba" (globális lista)
    users_db.append(user)
    
    # "Email küldés"
    email_message = f"""
    Kedves {name}!
    
    Sikeres regisztráció!
    Email: {email}
    Kategória: {category}
    Kedvezmény: {int(discount * 100)}%
    
    Üdvözlettel,
    A Csapat
    """
    print("\n Email elküldve:")
    print(email_message)
    email_log.append({"to": email, "message": email_message})
    
    # Statisztika számítás és kiírás
    print(f"\n Sikeres regisztráció!")
    print(f"Összes regisztrált felhasználó: {len(users_db)}")
    
    young_count = 0
    adult_count = 0
    senior_count = 0
    for u in users_db:
        if u["category"] == "fiatal":
            young_count += 1
        elif u["category"] == "felnőtt":
            adult_count += 1
        else:
            senior_count += 1
    
    print(f"Fiatallok: {young_count}, Felnőttek: {adult_count}, Nyugdíjasok: {senior_count}")
    
    # JSON export
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(users_db, f, ensure_ascii=False, indent=2)
    print(" Adatok mentve a users.json fájlba")
    
    return True


# Használat:
if __name__ == "__main__":
    register_user()
    print(f"\nAdatbázis: {users_db}")
