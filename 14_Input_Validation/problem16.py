print("List of operations: +; -; /; *")
operator = input("Enter the operator: ")

while operator != "+" and operator != "-" and operator != "/" and operator != "*":
    operator = input("Please enter a valid operator: ")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
while operator == "/" and b == 0:
    print("Division by 0 not possible")
    b = int(input("Re-enter the second number: "))

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
else:
    print(a / b)