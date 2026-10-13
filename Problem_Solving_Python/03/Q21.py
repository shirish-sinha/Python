discount20 = 0
discount15 = 0
discount10 = 0
discount_no = 0
total_discount = 0
total = 0

for i in range(10):
    price = int(input("Enter the price: "))

    if price < 1000:
        discount_no += 1
        total += price
    elif price < 3000:
        discount10 += 1
        total_discount += price * 0.1
        total += price + (price * 0.1)
    elif price < 5000:
        discount15 += 1
        total_discount += price * 0.15
        total += price + (price * 0.15)
    else:
        discount20 += 1
        total_discount += price * 0.2
        total += price + (price * 0.2)
print(f"Total: {total}")
print(f"10% Discount: {discount10}; 15% Discount: {discount15}; 20% Discount: {discount20}")
print(f"Total Discount: {total_discount}")