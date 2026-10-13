sum = 0
budget = 0
regular = 0
premium = 0
luxury = 0
for i in range(8):
    price = int(input("Enter the price: "))
    if price < 500:
        budget += 1
        print("Budget")
    elif price < 2000:
        regular += 1
        print("Regular")
    elif price < 5000:
        premium += 1
        print("Premium")
    else:
        luxury += 1
        print("Luxury")
    sum += price

print(f"Total: {sum}")
print(f"Budget: {budget}, Regular: {regular}, Premium: {premium}, Luxury: {luxury}")
print(f"Average: {sum/8}")