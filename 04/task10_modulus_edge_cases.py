# Task 10 - Modulus Edge Cases
# Test modulus with all sign combinations.

positive1 = 20
positive2 = 3
negative1 = -20
negative2 = -3

print("positive % positive:", positive1, "%", positive2, "=", positive1 % positive2)
print("negative % positive:", negative1, "%", positive2, "=", negative1 % positive2)
print("positive % negative:", positive1, "%", negative2, "=", positive1 % negative2)
print("negative % negative:", negative1, "%", negative2, "=", negative1 % negative2)

# Observation: In Python, the result of the modulus operator always
# takes the SIGN of the divisor (the right-hand operand), not the
# dividend. This is because % is defined in terms of floor division:
# a % b == a - (a // b) * b
