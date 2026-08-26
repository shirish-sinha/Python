# Task 13 - Boolean Arithmetic
# Arithmetic operations using True and False, with type() checks.

x = True
y = False

addition = x + y
subtraction = x - y
multiplication = x * y
division = x / 2   # division needs a non-zero divisor, using 2 for a valid result
floor_division = x // 2
modulus = x % 2
exponentiation = x ** 3

print("True + False =", addition, "| Type:", type(addition))
print("True - False =", subtraction, "| Type:", type(subtraction))
print("True * False =", multiplication, "| Type:", type(multiplication))
print("True / 2 =", division, "| Type:", type(division))
print("True // 2 =", floor_division, "| Type:", type(floor_division))
print("True % 2 =", modulus, "| Type:", type(modulus))
print("True ** 3 =", exponentiation, "| Type:", type(exponentiation))

# Note: Python treats True as 1 and False as 0 in arithmetic contexts.
# The result of +, -, and * between two booleans stays an int, while
# / always produces a float.
