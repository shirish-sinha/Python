# Problem 20

print("1 : Addition")
print("2 : Subtraction")
print("3 : Multiplication")
print("4 : Division")
print("5 : Floor Division")
number = int(input("Enter your choice number: "))
a = int(input("Enter your first integer: "))
b = int(input("Enter your 2nd integer: "))

match number:
    case 1:
        print(f"Addition is {a+b}")
    case 2:
        print(f"Subtraction is {a-b}")
    case 3:
        print(f"Multiplication is {a*b}")
    case 4:
        print(f"Division is {a/b}")
    case 5:
        print(f"Floor Division is {a//b}")
    case _:
        print("Invalid choice number")
