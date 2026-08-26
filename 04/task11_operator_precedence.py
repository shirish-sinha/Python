# Task 11 - Operator Precedence
# Evaluate expressions and explain the order of operations.

# Expression 1: 10 + 5 * 2
result1 = 10 + 5 * 2
print("10 + 5 * 2 =", result1)
# Explanation: * has higher precedence than +, so 5 * 2 = 10 is evaluated
# first, then 10 + 10 = 20.

# Expression 2: 20 - 4 / 2
result2 = 20 - 4 / 2
print("20 - 4 / 2 =", result2)
# Explanation: / has higher precedence than -, so 4 / 2 = 2.0 is evaluated
# first, then 20 - 2.0 = 18.0.

# Expression 3: 10 + 20 / 5 * 2
result3 = 10 + 20 / 5 * 2
print("10 + 20 / 5 * 2 =", result3)
# Explanation: / and * have equal precedence and are evaluated left to
# right before +. So 20 / 5 = 4.0 first, then 4.0 * 2 = 8.0, then
# 10 + 8.0 = 18.0.

# Expression 4: 2 + 3 * 4 ** 2
result4 = 2 + 3 * 4 ** 2
print("2 + 3 * 4 ** 2 =", result4)
# Explanation: ** has the highest precedence, so 4 ** 2 = 16 is evaluated
# first, then 3 * 16 = 48, then 2 + 48 = 50.

# Expression 5: 100 - 20 // 5
result5 = 100 - 20 // 5
print("100 - 20 // 5 =", result5)
# Explanation: // has higher precedence than -, so 20 // 5 = 4 is
# evaluated first, then 100 - 4 = 96.
