import json
from datetime import date
# ========== VALIDÁCIÓ ==========
def is_valid_email(email):
    if "@" not in email:
        return False
    parts=email.split("@")
    if len(parts)!=2:
        return False
    return "." in parts[1]
# asd@fgh.jk
# [0]=>asd
# [1]=>fgh.jk

def is_valid_password(password):
    if len(password)<8:
        return False
    has_digit=any(char.isdigit() for char in password)
    has_letter=any(char.isalpha() for char in password)
    return has_digit and has_letter

def is_valid_age(age):
    return 18 <=age <=120

def is_valid_name(name):
    return len(name)>=2

# ========== ÜZLETI LOGIKA ==========
def determine_user_category(age):
    if age < 25:
        return "fiatal"
    elif age < 65:
        return "felnőtt"
    else:
        return "nyugdíjas"

def calculate_discount(category):
    discounts={
        "fiatal":0.1,
        "felnőtt":0.0,
        "nyugdíjas":0.15
    }
    return discounts.get(category,0.0)

def create_user(email,password,name,age):
    category=determine_user_category(age)
    discount=calculate_discount(category)
    
    return {
        "email": email,
        "password": password,
        "name": name,
        "age": age,
        "category": category,
        "discount": discount,
        "registration_date": str(date.today()),
        "active": True
    }
    
def email_exists(email,users):
    return any(user["email"]==email for user in users)

def create_welcome_email(user):
    return f"""
    Kedves {user['name']}!
    
    Sikeres regisztráció!
    Email: {user['email']}
    Kategória: {user['category']}
    Kedvezmény: {int(user['discount'] * 100)}%
    
    Üdvözlettel,
    A Csapat
    """
    
def calculate_statistics(users):
    stats={"fiatal":0 , "felnőtt":0, "nyugdíjas":0}
    
    for user in users:
        category = user["category"]
        if category in stats:
            stats[category]+=1
    return stats

# ========== INPUT KEZELÉS ==========

def read_email(users):
    while True:
        email=input("Email cím: ")
        if not is_valid_email(email):
            print("HIBA: Hibás email formátum!")
            continue
        if email_exists(email,users):
            print("HIBA: Ez az email már regisztrálva van!")
            continue
        return email
    
def read_password():
    while True:
        password=input("Jelszó (min 8 karakter, kell szám és betű is): ")
        if not is_valid_password(password):
            print("HIBA: A jelszónak min 8 karakternek kell lennie és tartalmaznia kell egy számot és egy betűt")
            continue
        return password

def read_name():
    while True:
        name=input("Név: ")
        if not is_valid_name(name):
            print("HIBA: A név túl rövid")
            continue
        return name
        
def read_age():
    while True:
        try:
            age=input("Életkor:")
            if not is_valid_age(age):
                print("HIBA: Az életkornak 18 és 120 között kell lennie!")
                continue
            return age
        except ValueError:
            print("HIBA: Számot adj meg!")
            
# ========== OUTPUT KEZELÉS ==========

def print_welcome_message(email_text):
    print("\nEmail eküldve:")
    print (email_text)
    
def print_statistics(total,stats):
    print(f"\nOK:Sikeres regisztráció!")
    print(f"Összes regisztrált felhasználó: {total}")
    print(f"Fiatalok:{stats['fiatal']}, Felnőttek:{stats['felnőtt']}, Nyugdíjasok:{stats['nyugdíjas']}, ")

def save_users_to_file(users,filename="users.json"):
    with open(filename,"w", encoding="utf-8") as f:
        json.dump(users,f,ensure_ascii=False,indent=2)
    print(f"Adatok mentve a {filename} fájlba")
    
# ========== KOORDINÁLÓ FÜGGVÉNY ==========
def register_user(users):
    print("=== Felhasználó regisztráció ===")
    
    #Input gyűjtés
    email=read_email(users)
    password=read_password()
    name=read_email()
    age=read_age()
    
    #Üzleti logika
    user=create_user(email,password,name,age)
    new_users=users+[user]#olyan mint az append, hozzáadjuk a meglévő userekhez
    #Immutable hozzáadás
    email_text=create_welcome_email(user)
    stats=calculate_statistics(new_users)
    
    #Output
    print_welcome_message(email_text)
    print_statistics(len(new_users),stats)
    save_users_to_file(new_users)
    
    return new_users,user

# ========== HASZNÁLAT ==========

if __name__ == "__main__":
    users_db = []
    users_db, new_user = register_user(users_db)
    print(f"\nÚj felhasználó: {new_user['email']}")