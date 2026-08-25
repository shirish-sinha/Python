value = 10
print(type(value))

value = "ten"
print(type(value))

# At first, value held an integer, so type() showed int.
# After reassignment, value holds a string, so type() showed str.
# This happened because Python variables do not have a fixed type,
# a variable simply refers to whatever value it was most recently
# assigned, and its type changes along with that value.
