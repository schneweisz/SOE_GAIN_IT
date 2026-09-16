"""
03 - E-COMMERCE RENDELÉS FELDOLGOZÁS - REFAKTORÁLT VERZIÓ
MEGOLDÁS: Tiszta függvények, szétválasztott felelősségek (OSZTÁLYOK NÉLKÜL)
"""



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


# ========== ADATSTRUKTÚRÁK ==========

def create_customer(name, email, address, customer_type):
    """Létrehoz egy vásárlót."""

    return True


def create_order_item(product, quantity, unit_price, 
                     quantity_discount, line_total):
    """Létrehoz egy rendelési tételt."""
    return True


def create_order(customer, items, subtotal,
                customer_discount, coupon_discount,
                shipping_cost, tax, total,
                shipping_method):
    """Létrehoz egy rendelést."""
    return True


# ========== VALIDÁCIÓ ==========

def is_valid_name(name):
    """Ellenőrzi a név érvényességét."""
    return True


def is_valid_email(email):
    """Ellenőrzi az email érvényességét."""
    return True


def is_valid_address(address):
    """Ellenőrzi a cím érvényességét."""
    return True


def has_enough_stock(product, quantity, inventory):
    """Ellenőrzi, hogy van-e elég készlet."""
    return True


# ========== ÜZLETI LOGIKA ==========

def calculate_quantity_discount(quantity):
    """Kiszámítja a mennyiségi kedvezményt."""
    return True


def calculate_line_total(unit_price, quantity):
    """Kiszámítja egy tétel végösszegét kedvezménnyel."""
    return True

def calculate_customer_discount(subtotal, customer_type):
    """Kiszámítja a vásárlói kedvezményt."""
    return True


def apply_coupon(code, amount):
    """Alkalmaz egy kupon kódot és visszaadja a kedvezmény összegét."""
    return True


def calculate_shipping_cost(amount, shipping_method, free_threshold = 500.0):
    """Kiszámítja a szállítási költséget."""
    return True


def calculate_tax(amount, tax_rate = 0.27):
    """Kiszámítja az ÁFA-t."""
    return True


def calculate_order_total(
    subtotal,
    customer_discount,
    coupon_discount,
    shipping_cost,
    tax_rate = 0.27
):
    """
    Kiszámítja a rendelés végösszegét.
    Visszaad: (tax, grand_total)
    """
    return True


# ========== KÉSZLET ==========

def update_inventory(inventory, product, quantity):
    """Frissíti a készletet (immutable)."""
    return True


def check_low_stock(inventory, threshold = 5):
    """Visszaadja az alacsony készletű termékeket."""
    return True


# ========== FORMÁZÁS ==========

def format_invoice(order, order_number):
    """Formázza a számlát."""
    return True


def format_confirmation_email(order, order_number):
    """Formázza a visszaigazóló emailt."""
    return True


def format_inventory_status(inventory):
    """Formázza a készlet státuszt."""
    return True


# ========== INPUT FÜGGVÉNYEK ==========

def read_customer_name():
    """Bekér egy érvényes nevet."""
    return True


def read_customer_email():
    """Bekér egy érvényes email címet."""
    return True


def read_customer_address():
    """Bekér egy érvényes címet."""
    return True


def read_customer_type():
    """Bekéri a vásárló típusát."""
    return True


def read_order_items(
    inventory,
    prices
):
    """
    Bekéri a rendelési tételeket.
    Visszaad: (items, updated_inventory)
    """
    return True


def read_coupon_code():
    """Bekéri a kupon kódot."""
    return True


def read_shipping_method():
    """Bekéri a szállítási módot."""
    return True


# ========== KOORDINÁLÓ FÜGGVÉNY ==========

def process_order(
    inventory,
    prices,
    existing_orders
):
    """
    Feldolgoz egy rendelést.
    Visszaad: (order or None, updated_inventory)
    """
    return True


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
