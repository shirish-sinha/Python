amt = int(input("Enter an amount: "))

if amt > 0:
    if amt < 500:
        print("Discount: 0%")
        print(f"Discount amount: {0 * amt}")
        print(f"Final amount: {amt - (0 * amt)}")
    elif amt < 1000:
        print("Discount: 5%")
        print(f"Discount amount: {0.05 * amt}")
        print(f"Final amount: {amt - (0.05 * amt)}")
    elif amt < 2000:
        print("Discount: 10%")
        print(f"Discount amount: {0.1 * amt}")
        print(f"Final amount: {amt - (0.1 * amt)}")
    elif amt < 5000:
        print("Discount: 15%")
        print(f"Discount amount: {0.15 * amt}")
        print(f"Final amount: {amt - (0.15 * amt)}")
    else:
        print("Discount: 20%")
        print(f"Discount amount: {0.2 * amt}")
        print(f"Final amount: {amt - (0.2 * amt)}")
else:
    print("Please enter a valid amount")