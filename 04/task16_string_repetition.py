# Task 16 - String Repetition
# Repeat a string using * and observe what happens with a float multiplier.

word = "Python"

repeated_word = word * 3
print("word * 3 =", repeated_word)

# Now try multiplying the string by a float
try:
    result = word * 2.5
    print("word * 2.5 =", result)
except TypeError as e:
    print("word * 2.5 raised an error:", e)

# Observation: The * operator only works between a string and an
# integer. Multiplying a string by a float raises a TypeError because
# Python cannot repeat a string a fractional number of times.
