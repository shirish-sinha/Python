# Task 21 - Arithmetic Expression Analyzer
# Using a = 10, b = -3, c = 2.5, create and analyze at least 10 expressions.
# For each: write it, predict the result, run it, compare, and explain if wrong.

a = 10
b = -3
c = 2.5

expressions = [
    # (description, prediction, function that computes the actual result)
    ("a + b",             7,      lambda: a + b),
    ("a - b",             13,     lambda: a - b),
    ("a * b",             -30,    lambda: a * b),
    ("a / b",             -3.3333333333333335, lambda: a / b),
    ("a // b",            -4,     lambda: a // b),
    ("a % b",             -2,     lambda: a % b),
    ("a ** 2",            100,    lambda: a ** 2),
    ("(a + b) * c",       17.5,   lambda: (a + b) * c),
    ("a + b * c",         2.5,    lambda: a + b * c),
    ("a / b + c",         -0.8333333333333335, lambda: a / b + c),
    ("(a - c) // 2",      3,      lambda: (a - c) // 2),
    ("-b ** 2",           -9,     lambda: -b ** 2),
    ("(-b) ** 2",         9,      lambda: (-b) ** 2),
]

print(f"a = {a}, b = {b}, c = {c}")
print("=" * 70)

for expr_text, prediction, func in expressions:
    actual = func()
    matched = "MATCH" if actual == prediction else "MISMATCH"
    print(f"Expression : {expr_text}")
    print(f"Prediction : {prediction}")
    print(f"Actual     : {actual}")
    print(f"Result     : {matched}")
    print("-" * 70)

# Notes on tricky ones:
# - "a / b" and "a / b + c" are floating point results and predictions
#   used enough decimal digits to match Python's float representation.
# - "a // b" = 10 // -3 = -4 because floor division rounds toward
#   negative infinity (-3.33... floors to -4), not toward zero.
# - "a % b" = 10 % -3 = -2 because the result of % always takes the
#   sign of the divisor (here, negative).
# - "-b ** 2" = -((-3) ** 2)? No: ** binds tighter than unary -, but
#   b is already negative (-3), so -b ** 2 means -(b ** 2) = -((-3)**2)
#   = -(9) = -9. Adding parentheses around (-b) forces -b = 3 to be
#   squared first, giving (-b) ** 2 = 3 ** 2 = 9. This shows how
#   parentheses and operator precedence change results with negative
#   numbers involved.
