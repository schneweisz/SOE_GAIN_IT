# ========== KONSTANSOK - VÁSÁRLÓ TÍPUSOK ==========

CUSTOMER_TYPES = {
    "normal": {"name": "Normál", "discount": 0.0},
    "premium": {"name": "Prémium", "discount": 0.1},
    "vip": {"name": "VIP", "discount": 0.2}
}


# ========== KONSTANSOK - SZÁLLÍTÁSI MÓDOK ==========

SHIPPING_METHODS = {
    "standard": {"name": "Standard", "cost": 10.0, "delivery_time": "5-7 nap"},
    "express": {"name": "Express", "cost": 25.0, "delivery_time": "2-3 nap"},
    "immediate": {"name": "Azonnal", "cost": 50.0, "delivery_time": "1 nap"}
}


# ========== FACTORY FÜGGVÉNYEK - ADATSTRUKTÚRÁK ==========

def create_customer(name, email, address, customer_type):
    """Létrehoz egy vásárlót."""
    return {
        "name": name,
        "email": email,
        "address": address,
        "customer_type": customer_type
    }


def create_order_item(product, quantity, unit_price, quantity_discount, line_total):
    """Létrehoz egy rendelési tételt."""
    return {
        "product": product,
        "quantity": quantity,
        "unit_price": unit_price,
        "quantity_discount": quantity_discount,
        "line_total": line_total
    }


def create_order(
    customer,
    items,
    subtotal,
    customer_discount,
    coupon_discount,
    shipping_cost,
    tax,
    total,
    shipping_method,
):
    """Létrehoz egy rendelést."""
    return {
        "customer": customer,
        "items": items,
        "subtotal": subtotal,
        "customer_discount": customer_discount,
        "coupon_discount": coupon_discount,
        "shipping_cost": shipping_cost,
        "tax": tax,
        "total": total,
        "shipping_method": shipping_method
    }


# ========== VALIDÁCIÓ ==========

def is_valid_name(name):
    """Ellenőrzi a név érvényességét."""
    return len(name) >= 2


def is_valid_email(email):
    """Ellenőrzi az email érvényességét."""
    return "@" in email


def is_valid_address(address):
    """Ellenőrzi a cím érvényességét."""
    return len(address) >= 10


def has_enough_stock(product, quantity, inventory):
    """Ellenőrzi, hogy van-e elég készlet."""
    return product in inventory and inventory[product] >= quantity


# ========== ÁR SZÁMÍTÁS ==========

def calculate_quantity_discount(quantity):
    """Kiszámítja a mennyiségi kedvezményt."""
    if quantity >= 10:
        return 0.05
    elif quantity >= 5:
        return 0.02
    return 0.0


def calculate_line_total(unit_price, quantity):
    """Kiszámítja egy tétel végösszegét kedvezménnyel."""
    discount = calculate_quantity_discount(quantity)
    return unit_price * quantity * (1 - discount)


def calculate_customer_discount(subtotal, customer_type):
    """Kiszámítja a vásárlói kedvezményt."""
    return subtotal * CUSTOMER_TYPES[customer_type]["discount"]


def apply_coupon(code, amount):
    """Alkalmaz egy kupon kódot és visszaadja a kedvezmény összegét."""
    coupons = {
        "SAVE10": amount * 0.1,
        "SAVE20": amount * 0.2,
        "WELCOME": 15.0
    }
    return coupons.get(code.upper(), 0.0)


def calculate_shipping_cost(amount, shipping_method, free_threshold=500.0):
    """Kiszámítja a szállítási költséget."""
    if amount >= free_threshold:
        return 0.0
    return SHIPPING_METHODS[shipping_method]["cost"]


def calculate_tax(amount, tax_rate=0.27):
    """Kiszámítja az ÁFA-t."""
    return amount * tax_rate


def calculate_order_total(
    subtotal,
    customer_discount,
    coupon_discount,
    shipping_cost,
    tax_rate=0.27,
):
    """
    Kiszámítja a rendelés végösszegét.
    Visszaad: (tax, grand_total)
    """
    after_discounts = subtotal - customer_discount - coupon_discount
    before_tax = after_discounts + shipping_cost
    tax = calculate_tax(before_tax, tax_rate)
    grand_total = before_tax + tax
    return tax, grand_total


# ========== KÉSZLET ==========

def update_inventory(inventory, product, quantity):
    """Frissíti a készletet (immutable)."""
    new_inventory = inventory.copy()
    new_inventory[product] -= quantity
    return new_inventory


def check_low_stock(inventory, threshold=5):
    """Visszaadja az alacsony készletű termékeket."""
    return [product for product, stock in inventory.items() if stock < threshold]


# ========== FORMÁZÁS ==========

def format_invoice(order, order_number):
    """Formázza a számlát."""
    customer = order["customer"]
    customer_type_info = CUSTOMER_TYPES[customer["customer_type"]]
    shipping_info = SHIPPING_METHODS[order["shipping_method"]]
    
    lines = [
        "=" * 50,
        "SZÁMLA",
        "=" * 50,
        f"Vásárló: {customer['name']}",
        f"Email: {customer['email']}",
        f"Cím: {customer['address']}",
        f"Típus: {customer_type_info['name']}",
        "\nTételek:"
    ]
    
    for item in order["items"]:
        lines.append(f"  {item['quantity']}x {item['product']}")
        lines.append(f"    Egységár: ${item['unit_price']:.2f}")
        if item["quantity_discount"] > 0:
            lines.append(f"    Mennyiségi kedvezmény: {int(item['quantity_discount']*100)}%")
        lines.append(f"    Részösszeg: ${item['line_total']:.2f}")
    
    lines.append(f"\nRészösszeg: ${order['subtotal']:.2f}")
    
    if order["customer_discount"] > 0:
        lines.append(f"Vásárlói kedvezmény: -${order['customer_discount']:.2f}")
    
    if order["coupon_discount"] > 0:
        lines.append(f"Kupon kedvezmény: -${order['coupon_discount']:.2f}")
    
    lines.append(f"Szállítás ({shipping_info['name']}): ${order['shipping_cost']:.2f}")
    lines.append(f"Áfa (27%): ${order['tax']:.2f}")
    lines.append(f"\n{'VÉGÖSSZEG':.<30}${order['total']:.2f}")
    lines.append("=" * 50)
    
    return "\n".join(lines)


def format_confirmation_email(order, order_number):
    """Formázza a visszaigazóló emailt."""
    customer = order["customer"]
    shipping_info = SHIPPING_METHODS[order["shipping_method"]]
    
    return f"""Kedves {customer['name']}!

Köszönjük a rendelését!

Rendelés száma: #{order_number}
Végösszeg: ${order['total']:.2f}
Szállítási mód: {shipping_info['name']} ({shipping_info['delivery_time']})

Hamarosan útnak indul!

Üdvözlettel,
E-Shop Csapat"""


def format_inventory_status(inventory):
    """Formázza a készlet státuszt."""
    lines = ["Aktuális készlet:"]
    low_stock = check_low_stock(inventory)
    
    for product, stock in inventory.items():
        if product in low_stock:
            lines.append(f"  FIGYELEM: {product}: {stock} db (ALACSONY!)")
        else:
            lines.append(f"  OK: {product}: {stock} db")
    
    return "\n".join(lines)


# ========== INPUT FÜGGVÉNYEK ==========

def read_customer_name():
    """Bekér egy érvényes nevet."""
    while True:
        name = input("Vásárló neve: ")
        if is_valid_name(name):
            return name
        print("HIBA: A név túl rövid!")


def read_customer_email():
    """Bekér egy érvényes email címet."""
    while True:
        email = input("Email cím: ")
        if is_valid_email(email):
            return email
        print("HIBA: Érvénytelen email!")


def read_customer_address():
    """Bekér egy érvényes címet."""
    while True:
        address = input("Szállítási cím: ")
        if is_valid_address(address):
            return address
        print("HIBA: A cím túl rövid!")


def read_customer_type():
    """Bekéri a vásárló típusát."""
    print("\nVásárló típusa:")
    print("1. Normál")
    print("2. Prémium (10% kedvezmény)")
    print("3. VIP (20% kedvezmény)")
    
    choice = input("Válassz (1-3): ")
    
    type_map = {
        "1": "normal",
        "2": "premium",
        "3": "vip"
    }
    
    return type_map.get(choice, "normal")


def read_order_items(inventory, prices):
    """
    Bekéri a rendelési tételeket.
    Visszaad: (items, updated_inventory)
    """
    items = []
    current_inventory = inventory.copy()
    
    while True:
        print("\nElérhető termékek:")
        for product, stock in current_inventory.items():
            price = prices[product]
            print(f"  {product}: ${price} (raktáron: {stock} db)")
        
        product = input("\nTermék neve (vagy 'vége'): ").lower()
        
        if product == "vége":
            break
        
        if product not in current_inventory:
            print("HIBA: Nincs ilyen termék!")
            continue
        
        try:
            quantity = int(input(f"Mennyiség (max {current_inventory[product]} db): "))
        except ValueError:
            print("HIBA: Érvénytelen mennyiség!")
            continue
        
        if quantity <= 0:
            print("HIBA: A mennyiség pozitív kell legyen!")
            continue
        
        if not has_enough_stock(product, quantity, current_inventory):
            print(f"HIBA: Nincs elég készlet! (max {current_inventory[product]} db)")
            continue
        
        # Ár számítás
        unit_price = prices[product]
        quantity_discount = calculate_quantity_discount(quantity)
        line_total = calculate_line_total(unit_price, quantity)
        
        if quantity_discount > 0:
            print(f"{int(quantity_discount*100)}% mennyiségi kedvezmény!")
        
        # Készlet frissítése
        current_inventory = update_inventory(current_inventory, product, quantity)
        
        # Tétel hozzáadása
        item = create_order_item(product, quantity, unit_price, quantity_discount, line_total)
        items.append(item)
        print(f"OK: Hozzáadva: {quantity} x {product} (${line_total:.2f})")
    
    return items, current_inventory


def read_coupon_code():
    """Bekéri a kupon kódot."""
    return input("\nVan kupon kódod? (Enter = nincs): ").upper()


def read_shipping_method():
    """Bekéri a szállítási módot."""
    print("\nSzállítási mód:")
    print("1. Standard (5-7 nap) - $10")
    print("2. Express (2-3 nap) - $25")
    print("3. Azonnal (1 nap) - $50")
    
    choice = input("Válassz (1-3): ")
    
    method_map = {
        "1": "standard",
        "2": "express",
        "3": "immediate"
    }
    
    return method_map.get(choice, "standard")


# ========== KOORDINÁLÓ FÜGGVÉNY ==========

def process_order(inventory, prices, existing_orders):
    """
    Feldolgoz egy rendelést.
    Visszaad: (order or None, updated_inventory)
    """
    print("ÚJ RENDELÉS FELDOLGOZÁSA")
    print("="*50)
    
    # 1. Ügyfél adatok
    name = read_customer_name()
    email = read_customer_email()
    address = read_customer_address()
    customer_type = read_customer_type()
    
    customer = create_customer(name, email, address, customer_type)
    
    # 2. Rendelési tételek
    items, new_inventory = read_order_items(inventory, prices)
    
    if not items:
        print("HIBA: Üres rendelés!")
        return None, inventory
    
    # 3. Árak számítása
    subtotal = sum(item["line_total"] for item in items)
    customer_discount = calculate_customer_discount(subtotal, customer_type)
    
    # 4. Kupon
    coupon = read_coupon_code()
    after_customer_discount = subtotal - customer_discount
    coupon_discount = apply_coupon(coupon, after_customer_discount)
    
    if coupon_discount > 0:
        print(f"OK: Kupon alkalmazva: -${coupon_discount:.2f}")
    elif coupon:
        print("HIBA: Érvénytelen kupon!")
    
    # 5. Szállítás
    shipping_method = read_shipping_method()
    after_coupon = after_customer_discount - coupon_discount
    shipping_cost = calculate_shipping_cost(after_coupon, shipping_method)
    shipping_info = SHIPPING_METHODS[shipping_method]
    
    if after_coupon >= 500 and shipping_info["cost"] > 0:
        print("INGYENES SZÁLLÍTÁS $500+ rendelés esetén!")
    
    # 6. Végösszeg
    tax, total = calculate_order_total(
        subtotal, customer_discount, coupon_discount, shipping_cost
    )
    
    # 7. Rendelés létrehozása
    order = create_order(
        customer, items, subtotal, customer_discount,
        coupon_discount, shipping_cost, tax, total, shipping_method
    )
    
    # 8. Kimenetek
    order_number = len(existing_orders) + 1
    print("\n" + format_invoice(order, order_number))
    print(f"\nEmail elküldve: {email}")
    print(format_confirmation_email(order, order_number))
    print("\n" + format_inventory_status(new_inventory))
    
    return order, new_inventory


# ========== HASZNÁLAT ==========

if __name__ == "__main__":
    initial_inventory = {
        "laptop": 10,
        "mouse": 50,
        "keyboard": 30,
        "monitor": 15
    }
    
    product_prices = {
        "laptop": 1200.0,
        "mouse": 25.0,
        "keyboard": 75.0,
        "monitor": 350.0
    }
    
    all_orders = []
    current_inventory = initial_inventory
    
    order, current_inventory = process_order(current_inventory, product_prices, all_orders)
    
    if order:
        all_orders.append(order)
        total_revenue = sum(o["total"] for o in all_orders)
        print(f"\nMai összes bevétel: ${total_revenue:.2f}")
        print(f"Mai rendelések száma: {len(all_orders)}")
