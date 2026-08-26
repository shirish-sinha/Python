# Task 2 - Integer and Float
# One integer and one float, all applicable arithmetic operations between them.
# Display the result and the data type of the result for each operation.

int_num = 10
float_num = 3.5

addition = int_num + float_num
subtraction = int_num - float_num
multiplication = int_num * float_num
division = int_num / float_num
floor_division = int_num // float_num
modulus = int_num % float_num
exponentiation = int_num ** float_num

print("int_num =", int_num, "| float_num =", float_num)
print()

print("Addition:", addition, "| Type:", type(addition))
print("Subtraction:", subtraction, "| Type:", type(subtraction))
print("Multiplication:", multiplication, "| Type:", type(multiplication))
print("Division:", division, "| Type:", type(division))
print("Floor Division:", floor_division, "| Type:", type(floor_division))
print("Modulus:", modulus, "| Type:", type(modulus))
print("Exponentiation:", exponentiation, "| Type:", type(exponentiation))

# Note: Whenever an int and a float are combined in any arithmetic
# operation, Python automatically converts the result to a float.
