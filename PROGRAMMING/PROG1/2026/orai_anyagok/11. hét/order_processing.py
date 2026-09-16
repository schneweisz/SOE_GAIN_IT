OrderItem=tuple[str,float,int]
# _ (vszeg név, egységár, darabszám)

from typing import Optional

def calculate_subtotal(items:list[OrderItem])->float:
    return sum(unit_price*quantity for _,unit_price, quantity in items)


def calculate_discount(
    items: list[OrderItem], is_vip: bool, coupon_percent: Optional[float]
) -> float:
    subtotal = calculate_subtotal(items)
    vip_discount = 0.1 if is_vip else 0.0
    coupon_discount = (coupon_percent or 0.0) / 100
    discount_rate = min(vip_discount + coupon_discount, 0.5)
    return subtotal * discount_rate

def calculate_final_total(
    items:list[OrderItem],is_vip:bool,coupon_percent:float
)->float:
    subtotal=calculate_subtotal(items)
    discount=calculate_discount(items,is_vip,coupon_percent)
    shipping_cost=0.0 if subtotal>=100 else 12.0
    return subtotal- discount+shipping_cost

def build_shipping_label(
    order_id:int,costumer_name:str,status:str
)->str:
    if status!="paid":
        return None
    return f"ORDER-{order_id} | {costumer_name}"