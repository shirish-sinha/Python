limit = int(input("Enter a non-negative integer: "))
if limit < 0:
    print("Factorial is not defined for negative numbers.")
else:
    number = 1
    product = 1
    while number <= limit:
        product *= number
        number += 1
    print("Factorial:", product)