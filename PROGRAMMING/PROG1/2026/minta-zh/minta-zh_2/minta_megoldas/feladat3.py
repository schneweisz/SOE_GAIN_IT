OrderItem = tuple[str, float, int]


def calculate_subtotal(items: list[OrderItem]) -> float:
    """Kiszámolja a rendelési tételek részösszegét.

    >>> calculate_subtotal([])
    0.0
    >>> calculate_subtotal([("alma", 10.0, 2), ("korte", 5.5, 4)])
    42.0
    """
    total = 0.0
    for _, unit_price, quantity in items:
        total += unit_price * quantity
    return total


def calculate_discount(
    items: list[OrderItem], is_vip: bool, coupon_percent: float | None
) -> float:
    """Kiszámolja a rendelés kedvezményének összegét.

    >>> calculate_discount([("termek", 100.0, 1)], True, None)
    10.0
    >>> calculate_discount([("termek", 200.0, 1)], False, 25)
    50.0
    >>> calculate_discount([("termek", 100.0, 1)], True, 80)
    50.0
    """
    subtotal = calculate_subtotal(items)
    vip_discount = 0.1 if is_vip else 0.0
    coupon_discount = 0.0 if coupon_percent is None else coupon_percent / 100
    discount_rate = min(vip_discount + coupon_discount, 0.5)
    return subtotal * discount_rate


def calculate_final_total(
    items: list[OrderItem], is_vip: bool, coupon_percent: float | None
) -> float:
    """Kiszámolja a kedvezménnyel és szállítással növelt végösszeget.

    >>> calculate_final_total([], False, None)
    12.0
    >>> calculate_final_total([("termek", 100.0, 1)], False, None)
    100.0
    >>> calculate_final_total([("termek", 80.0, 1)], True, None)
    84.0
    """
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(items, is_vip, coupon_percent)
    shipping_cost = 0.0 if subtotal >= 100 else 12.0
    return subtotal - discount + shipping_cost


def build_shipping_label(
    order_id: int, customer_name: str, status: str
) -> str | None:
    """Szállítási címkét készít fizetett rendeléshez.

    >>> build_shipping_label(42, "Anna Kovacs", "paid")
    'ORDER-42 | Anna Kovacs'
    >>> build_shipping_label(42, "Anna Kovacs", "pending") is None
    True
    """
    if status != "paid":
        return None
    return f"ORDER-{order_id} | {customer_name}"
