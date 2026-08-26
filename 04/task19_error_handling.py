# Task 19 - Error Handling Practice
# Demonstrate ZeroDivisionError, invalid string arithmetic, and arithmetic with None.

# 1. Division by Zero
print("--- Division by Zero ---")
try:
    result = 10 / 0
    print("Result:", result)
except ZeroDivisionError as e:
    print("Error raised: ZeroDivisionError ->", e)

print()

# 2. Invalid String Arithmetic
print("--- Invalid String Arithmetic ---")
try:
    result = "Hello" - "World"
    print("Result:", result)
except TypeError as e:
    print("Error raised: TypeError ->", e)

print()

# 3. Arithmetic with None
print("--- Arithmetic with None ---")
try:
    value = None
    result = value + 5
    print("Result:", result)
except TypeError as e:
    print("Error raised: TypeError ->", e)

# Summary:
# 10 / 0            -> ZeroDivisionError (division by zero is undefined)
# "Hello" - "World"  -> TypeError (subtraction is not defined for strings)
# None + 5          -> TypeError (arithmetic is not defined for NoneType)
