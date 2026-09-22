operator = input("Enter an operation (+, -, *, /): ")
num1 = float(input("Enter first number: " ))
num2 = float(input("Enter second number: " ))

if operator == "+":
    print(f"Sum = {num1 + num2}")
elif operator == "-":
    print(f"Difference = {num1 - num2}")
elif operator == "*":
    print(f"Product = {num1 * num2}")
elif operator == "/" and num2 != 0:
    print(f"Quotient = (num1 / num2)")
    print(f"Remainder = {num1 % num2}")
else:
    print("You did not choose a valid operation!")