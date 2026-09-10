unit = 129

if unit < 0:
    print("Please enter a valid value")
elif unit <= 100:
    print("Bill = ", unit * 5)
elif unit <= 200:
    print("Bill = ", unit * 7)
else:
    print("Bill = ", unit * 10)