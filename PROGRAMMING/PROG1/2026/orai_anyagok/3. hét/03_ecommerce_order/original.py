"""
03 - E-COMMERCE RENDELÉS FELDOLGOZÁS
PROBLÉMA: Ez a függvény túl sok dolgot csinál egyszerre!
"""

inventory = {
    "laptop": 10,
    "mouse": 50,
    "keyboard": 30,
    "monitor": 15
}

prices = {
    "laptop": 1200.0,
    "mouse": 25.0,
    "keyboard": 75.0,
    "monitor": 350.0
}

orders = []
total_revenue = 0.0

def process_order():
    """
    EZ EGY ROSSZ FÜGGVÉNY!
    - Input kezelés
    - Validálás
    - Készlet ellenőrzés és módosítás
    - Ár számítás (több kedvezmény típus)
    - Szállítási költség számítás
    - Rendelés mentés
    - Email értesítés
    - Számla generálás
    - Globális változók módosítása
    """
    global inventory, total_revenue
    
    print(" ÚJ RENDELÉS FELDOLGOZÁSA")
    print("="*50)
    
    # Ügyfél adatok
    name = input("Vásárló neve: ")
    while len(name) < 2:
        print(" A név túl rövid!")
        name = input("Vásárló neve: ")
    
    email = input("Email cím: ")
    while "@" not in email:
        print(" Érvénytelen email!")
        email = input("Email cím: ")
    
    address = input("Szállítási cím: ")
    while len(address) < 10:
        print(" A cím túl rövid!")
        address = input("Szállítási cím: ")
    
    # Vásárlói típus
    print("\nVásárló típusa:")
    print("1. Normál")
    print("2. Prémium (10% kedvezmény)")
    print("3. VIP (20% kedvezmény)")
    customer_type = input("Válassz (1-3): ")
    
    if customer_type == "1":
        discount_rate = 0.0
        ctype = "normal"
    elif customer_type == "2":
        discount_rate = 0.1
        ctype = "premium"
    elif customer_type == "3":
        discount_rate = 0.2
        ctype = "vip"
    else:
        print(" Érvénytelen választás, normál vásárló lesz")
        discount_rate = 0.0
        ctype = "normal"
    
    # Termékek hozzáadása
    order_items = []
    subtotal = 0.0
    
    while True:
        print("\n Elérhető termékek:")
        for product, stock in inventory.items():
            price = prices[product]
            print(f" {product}: ${price} (raktáron: {stock} db)")
        
        product = input("\nTermék neve (vagy 'vége'): ").lower()
        
        if product == "vége":
            break
        
        if product not in inventory:
            print(" Nincs ilyen termék!")
            continue
        
        # Mennyiség bekérése
        try:
            quantity = int(input(f"Mennyiség (max {inventory[product]} db): "))
        except ValueError:
            print(" Érvénytelen mennyiség!")
            continue
        
        if quantity <= 0:
            print(" A mennyiség pozitív kell legyen!")
            continue
        
        if quantity > inventory[product]:
            print(f" Nincs elég készlet! (max {inventory[product]} db)")
            continue
        
        # Ár számítás
        unit_price = prices[product]
        line_total = unit_price * quantity
        
        # Mennyiségi kedvezmény
        if quantity >= 10:
            quantity_discount = 0.05
            print(f" 10+ darab: 5% mennyiségi kedvezmény!")
        elif quantity >= 5:
            quantity_discount = 0.02
            print(f" 5+ darab: 2% mennyiségi kedvezmény!")
        else:
            quantity_discount = 0.0
        
        line_total = line_total * (1 - quantity_discount)
        
        # Készlet frissítése
        inventory[product] -= quantity
        
        # Tétel hozzáadása
        order_items.append({
            'product': product,
            'quantity': quantity,
            'unit_price': unit_price,
            'quantity_discount': quantity_discount,
            'line_total': line_total
        })
        
        subtotal += line_total
        print(f" Hozzáadva: {quantity} x {product} (${line_total:.2f})")
    
    if not order_items:
        print(" Üres rendelés!")
        return False
    
    # Vásárlói kedvezmény alkalmazása
    discount_amount = subtotal * discount_rate
    after_discount = subtotal - discount_amount
    
    # Kupon kód
    coupon = input("\nVan kupon kódod? (Enter = nincs): ").upper()
    coupon_discount = 0.0
    
    if coupon == "SAVE10":
        coupon_discount = after_discount * 0.1
        print(" SAVE10 kupon: 10% kedvezmény!")
    elif coupon == "SAVE20":
        coupon_discount = after_discount * 0.2
        print(" SAVE20 kupon: 20% kedvezmény!")
    elif coupon == "WELCOME":
        coupon_discount = 15.0
        print(" WELCOME kupon: $15 kedvezmény!")
    elif coupon:
        print(" Érvénytelen kupon!")
    
    after_coupon = after_discount - coupon_discount
    
    # Szállítási költség
    print("\nSzállítási mód:")
    print("1. Standard (5-7 nap) - $10")
    print("2. Express (2-3 nap) - $25")
    print("3. Azonnal (1 nap) - $50")
    
    shipping_choice = input("Válassz (1-3): ")
    
    if shipping_choice == "1":
        shipping_cost = 10.0
        shipping_method = "Standard"
    elif shipping_choice == "2":
        shipping_cost = 25.0
        shipping_method = "Express"
    elif shipping_choice == "3":
        shipping_cost = 50.0
        shipping_method = "Azonnal"
    else:
        shipping_cost = 10.0
        shipping_method = "Standard"
        print(" Standard szállítás kiválasztva")
    
    # Ingyenes szállítás $500 felett
    if after_coupon >= 500:
        print(" INGYENES SZÁLLÍTÁS $500+ rendelés esetén!")
        shipping_cost = 0.0
    
    # Végösszeg
    total = after_coupon + shipping_cost
    
    # ÁFA (27%)
    tax = total * 0.27
    grand_total = total + tax
    
    # Számla kiírása
    print("\n" + "="*50)
    print(" SZÁMLA")
    print("="*50)
    print(f"Vásárló: {name}")
    print(f"Email: {email}")
    print(f"Cím: {address}")
    print(f"Típus: {ctype}")
    print("\nTételek:")
    for item in order_items:
        print(f" {item['quantity']}x {item['product']}")
        print(f" Egységár: ${item['unit_price']:.2f}")
        if item['quantity_discount'] > 0:
            print(f" Mennyiségi kedvezmény: {int(item['quantity_discount']*100)}%")
        print(f" Részösszeg: ${item['line_total']:.2f}")
    
    print(f"\nRészösszeg: ${subtotal:.2f}")
    if discount_amount > 0:
        print(f"Vásárlói kedvezmény ({ctype}): -${discount_amount:.2f}")
    if coupon_discount > 0:
        print(f"Kupon kedvezmény: -${coupon_discount:.2f}")
    print(f"Szállítás ({shipping_method}): ${shipping_cost:.2f}")
    print(f"Áfa (27%): ${tax:.2f}")
    print(f"\n{'VÉGÖSSZEG':.<30}${grand_total:.2f}")
    print("="*50)
    
    # Rendelés mentése
    order = {
        'customer': {'name': name, 'email': email, 'address': address, 'type': ctype},
        'items': order_items,
        'subtotal': subtotal,
        'discount': discount_amount + coupon_discount,
        'shipping': shipping_cost,
        'tax': tax,
        'total': grand_total
    }
    orders.append(order)
    total_revenue += grand_total
    
    # Email szimuláció
    email_body = f"""
Kedves {name}!

Köszönjük a rendelését!

Rendelés száma: #{len(orders)}
Végösszeg: ${grand_total:.2f}
Szállítási mód: {shipping_method}

Hamarosan útnak indul!

Üdvözlettel,
E-Shop Csapat
"""
    print(f"\n Email elküldve: {email}")
    print(email_body)
    
    # Készlet figyelmeztetés
    print("\n Aktuális készlet:")
    for product, stock in inventory.items():
        if stock < 5:
            print(f" {product}: {stock} db (ALACSONY!)")
        else:
            print(f" {product}: {stock} db")
    
    print(f"\n Mai összes bevétel: ${total_revenue:.2f}")
    print(f" Mai rendelések száma: {len(orders)}")
    
    return True


# Használat:
if __name__ == "__main__":
    process_order()
