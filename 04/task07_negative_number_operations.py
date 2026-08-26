# Task 7 - Negative Number Operations
# Two negative numbers, all basic arithmetic operations performed on them.

num1 = -12
num2 = -5

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2

print("num1 =", num1, "| num2 =", num2)
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)

# Observation: multiplying/dividing two negatives gives a positive result,
# while addition stays negative and floor division/modulus round toward
# negative infinity, which can look surprising at first glance.
