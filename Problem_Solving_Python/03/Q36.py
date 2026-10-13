revenue = 0
for i in range(5):
    name = input("Enter your name: ")
    member = input("Are you a member(y/n): ").lower()
    subtotal = 0
    total = 0
    if member == "y":
        is_member = True
    elif member == "n":
        is_member = False
    else:
        print("U did not enter a valid choice.")
    for j in range(3):
        price = int(input("Enter the price: "))
        subtotal += price
    if subtotal >= 2000:
        total = subtotal - subtotal * 0.15
    elif subtotal >= 1000:
        total = subtotal - subtotal * 0.1
    else:
        total = subtotal
    if is_member:
        total = total - total * 0.05
    print(f"Total: {total}")
    revenue += total
print(f"Revenue: {revenue}")