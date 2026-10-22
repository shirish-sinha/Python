total = 0
for i in range(8):
    age = int(input("Enter the age: "))
    distance = float(input("Enter the distance: "))

    fare = 10 * distance

    if age < 5:
        fare -= fare
    elif age < 12:
        fare -= fare * 0.5
    elif age >= 60:
        fare -= fare * 0.3

    total += fare
    print(f"Fare: {fare}")