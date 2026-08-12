cart_items = []
cart_total = len(cart_items)
shipping_speed = (input("What will be your shipping speed?: "))

def calculate_checkout(cart_total, shipping_speed):
    if shipping_speed == "Express":
        print("Shipping is 20.")
    elif shipping_speed =="Overnight":
        print("Shipping is 35.")
    elif shipping_speed == "Standard" and cart_total >= 100:
        print("Shipping is free or 0.")
    elif shipping_speed =="Standard" and cart_total <= 99:
        print("Shipping is 10")

    return cart_total + shipping_speed

calculate_checkout(shipping_speed)