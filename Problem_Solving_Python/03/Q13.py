for i in range(6):
    bill = 0
    units = int(input("Enter the units: "))
    if units < 0:
        print("You did not enter valid units")
        break
    elif units <= 100:
        bill = 5 * units
    elif units <= 200:
        bill = 500 + (7 * (units - 100))
    elif units <= 400:
        bill = 1200 + (10 * (units - 200))
    else:
        bill = 3200 + (15 * (units - 400))

    print(bill)
    if bill < 1000:
        print("Low")
    elif bill < 3000:
        print("Medium")
    else:
        print("High")