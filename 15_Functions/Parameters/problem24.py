def apply_discount(price, discount=0):
    return price - price * discount / 100


print(apply_discount(200))
print(apply_discount(200, 15))
