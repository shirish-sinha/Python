# Task 18 - None Type
# Try arithmetic operations between None and an integer, observe errors.

value = None
number = 10

operations = {
    "Addition (value + number)": lambda: value + number,
    "Subtraction (value - number)": lambda: value - number,
    "Multiplication (value * number)": lambda: value * number,
    "Division (value / number)": lambda: value / number,
    "Floor Division (value // number)": lambda: value // number,
    "Modulus (value % number)": lambda: value % number,
    "Exponentiation (value ** number)": lambda: value ** number,
}

for name, operation in operations.items():
    try:
        result = operation()
        print(name, "=", result)
    except TypeError as e:
        print(name, "-> Error:", e)

# Explanation:
# None is a special data type representing "no value" and it is NOT a
# number. Python does not define any arithmetic behavior for the None
# type, so any attempt to use it with +, -, *, /, //, %, or ** raises
# a TypeError, since Python cannot combine a NoneType with an int.
