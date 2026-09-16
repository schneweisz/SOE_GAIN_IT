# 03 - E-Commerce Rendelés Feldolgozás Refaktorálás

A `process_order()` függvény **túl sok dolgot csinál**:

### Felelősségek:
1. Vásárló adatok bekérése (3 input + validáció)
2. Vásárló típus kiválasztása
3. Termékek hozzáadása (ciklusban)
4. Készlet ellenőrzés és frissítés
5. Többféle kedvezmény számítás (vásárlói, mennyiségi, kupon)
6. Szállítási költség számítás
7. ÁFA számítás
8. Számla formázás és kiírás
9. Email generálás és "küldés"
10. Készlet státusz ellenőrzés
11. Bevétel nyilvántartás
12. Három globális változó módosítása

### További problémák:
- Globális változók (`inventory`, `orders`, `total_revenue`)
- Hardcoded konstansok (árak, kedvezmények)
- Manuális if-else láncok (customer type, shipping)
- Nem tesztelhető
- Kód duplikáció
- Nehéz bővíteni új kedvezmény típussal

## Megoldás a refaktorált kódban (`refactored.py`)

### 1. Adatstruktúrák és Enum-ok

```python
CustomerType.NORMAL # enum konstansként
ShippingMethod.EXPRESS # enum konstansként

@dataclass Customer # típusos adatstruktúra
@dataclass OrderItem # egy tétel
@dataclass Order # teljes rendelés
```

### 2. Tiszta függvények - Validáció
- `is_valid_name()` - név ellenőrzés
- `is_valid_email()` - email ellenőrzés
- `is_valid_address()` - cím ellenőrzés
- `has_enough_stock()` - készlet ellenőrzés

### 3. Tiszta függvények - Ár számítás
- `calculate_quantity_discount()` - mennyiségi kedvezmény
- `calculate_line_total()` - tétel összege
- `calculate_customer_discount()` - vásárlói kedvezmény
- `apply_coupon()` - kupon alkalmazás
- `calculate_shipping_cost()` - szállítási költség
- `calculate_tax()` - ÁFA
- `calculate_order_total()` - végösszeg

### 4. Tiszta függvények - Készlet
- `update_inventory()` - immutable készlet frissítés
- `check_low_stock()` - alacsony készlet keresés

### 5. Tiszta függvények - Formázás
- `format_invoice()` - számla formázás
- `format_confirmation_email()` - email formázás
- `format_inventory_status()` - készlet kiírás

### 6. Input függvények (nem tiszta, izolált)
- `read_customer_name/email/address()`
- `read_customer_type()`
- `read_order_items()`
- `read_coupon_code()`
- `read_shipping_method()`

### 7. Koordináció
- `process_order()` - összehangolja a folyamatot

## Enum előnyei

**Eredeti (rossz):**
```python
if customer_type == "1":
 discount_rate = 0.0
 ctype = "normal"
elif customer_type == "2":
 discount_rate = 0.1
 ctype = "premium"
# ...
```

**Refaktorált (jó):**
```python
class CustomerType(Enum):
 NORMAL = ("normal", 0.0)
 PREMIUM = ("premium", 0.1)
 VIP = ("vip", 0.2)

# Használat:
customer_type.discount # 0.1
```

## Immutable vs Mutable

**Eredeti (mutable):**
```python
global inventory
inventory[product] -= quantity # Módosítja a globális állapotot!
```

**Refaktorált (immutable):**
```python
def update_inventory(inventory, product, quantity):
 new_inventory = inventory.copy()
 new_inventory[product] -= quantity
 return new_inventory # Új példány, régi érintetlen
```

## Előnyök

 **Tesztelhető**: Minden üzleti logika tiszta függvény 
 **Típusbiztos**: Enum-ok és dataclass-ok 
 **Bővíthető**: Új CustomerType vagy ShippingMethod könnyen hozzáadható 
 **Immutable**: Nincs mellékhatás, könnyebb debuggolni 
 **Olvasható**: Kis, egyértelmű függvények 
 **Karbantartható**: Változtatások lokalizáltak 
 **Újrafelhasználható**: Függvények más kontextusban is működnek

## Funkcionalitási módosítások

**Eredeti:**
- Globális állapot módosítás
- Nem lehet több rendelést utána feldolgozni (készlet elveszett)

**Refaktorált:**
- Visszaadja az új készlet állapotot
- Láncolható rendelések: `order1, inv1 = process_order(inv0, ...)`

## Tanulságok

1. **Enum használata** konstansok helyett
2. **Dataclass** az adatok strukturálására
3. **Immutable műveletek** (copy) a mellékhatások elkerülésére
4. **Tiszta számítási függvények** könnyebben tesztelhetők
5. **if-else láncok** → **dictionary/enum lookup**
6. **Globális állapot elkerülése** → paraméterek és visszatérési értékek

