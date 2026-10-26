def subtotal(price, quantity):
    return price * quantity

def discount_rate(amount):
    if amount >= 1000:
        return 0.10
    return 0

def shipping_fee(amount):
    if amount >= 500:
        return 0
    return 50

def final_total(price, quantity):
    amount = subtotal(price, quantity)
    discount = amount * discount_rate(amount)
    return amount - discount + shipping_fee(amount)

assert subtotal(200, 3) == 600
assert discount_rate(999) == 0
assert discount_rate(1000) == 0.10
assert shipping_fee(500) == 0

print("Order 1 total:", final_total(100, 2))
print("Order 2 total:", final_total(250, 4))
