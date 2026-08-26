# Task 12 - Parentheses
# Run both versions of each expression and compare the results.

# Pair 1
a1 = 10 + 5 * 2
a2 = (10 + 5) * 2
print("10 + 5 * 2 =", a1)
print("(10 + 5) * 2 =", a2)
print()

# Pair 2
b1 = 20 - 10 / 2
b2 = (20 - 10) / 2
print("20 - 10 / 2 =", b1)
print("(20 - 10) / 2 =", b2)
print()

# Pair 3
c1 = 2 + 3 * 4
c2 = (2 + 3) * 4
print("2 + 3 * 4 =", c1)
print("(2 + 3) * 4 =", c2)

# Explanation:
# Parentheses override the default operator precedence. Without
# parentheses, Python evaluates * and / before + and -. Parentheses
# force Python to evaluate the enclosed expression first, which can
# completely change the outcome, as shown above where each parenthesized
# version produces a different (usually larger) result.
