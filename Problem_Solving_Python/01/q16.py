unit = int(input("Enter the units: "))

if unit < 0:
    print("Please enter a valid value")
elif unit <= 100:
    print("Bill = ", unit * 5)
elif unit <= 200:
    print("Bill = ", (100 * 5) + ((unit - 100) * 7))
else:
    print("Bill = ", (100 * 5) + (100 * 7) + ((unit - 200) * 10))