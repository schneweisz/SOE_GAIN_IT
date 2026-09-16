TicketItem = tuple[str, float, int]

def calculate_subtotal(items: list[TicketItem]) -> float:
    """
    Kiszámolja a jegyek részösszegét.

    >>> calculate_subtotal([])
    0.0
    >>> calculate_subtotal([("Normal", 10.0, 2), ("VIP", 5.5, 4)])
    42.0
    """
    total = 0.0
    for _, unit_price, quantity in items:
        total += unit_price * quantity
    return total

def calculate_discount(
    items: list[TicketItem], is_student: bool, promo_percent: float | None
) -> float:
    """
    Kiszámolja a kedvezmény összegét (Max 60%).

    >>> calculate_discount([("Normal", 100.0, 1)], True, None)
    15.0
    >>> calculate_discount([("Normal", 200.0, 1)], False, 25)
    50.0
    >>> calculate_discount([("Normal", 100.0, 1)], True, 50)
    60.0
    """
    subtotal = calculate_subtotal(items)
    
    student_discount = 0.15 if is_student else 0.0
    promo_discount = 0.0 if promo_percent is None else promo_percent / 100
    
    discount_rate = min(student_discount + promo_discount, 0.6)
    return subtotal * discount_rate

def calculate_final_total(
    items: list[TicketItem], is_student: bool, promo_percent: float | None
) -> float:
    """
    Kiszámolja a végösszeget kedvezménnyel és kezelési díjjal.

    >>> calculate_final_total([], False, None)
    0.0
    >>> calculate_final_total([("Normal", 100.0, 1)], False, None)
    100.0
    >>> calculate_final_total([("Normal", 40.0, 1)], False, None)
    46.0
    """
    subtotal = calculate_subtotal(items)
    if subtotal == 0:
        return 0.0
        
    discount = calculate_discount(items, is_student, promo_percent)
    
    handling_fee = 0.0 if subtotal >= 80 else 6.0
    
    return subtotal - discount + handling_fee


def build_booking_code(
    booking_id: int, customer_name: str, status: str
) -> str | None:
    """
    Foglalási kódot készít confirmed státuszú rendeléshez.

    >>> build_booking_code(42, "Anna Kovacs", "confirmed")
    'BOOKING-42 | Anna Kovacs'
    >>> build_booking_code(42, "Anna Kovacs", "pending") is None
    True
    """
    
    if status != "confirmed":
        return None
    return f"BOOKING-{booking_id} | {customer_name}"
