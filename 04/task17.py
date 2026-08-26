# Task 17 - String Operations
# Try string + string, string - string, string * integer, string / string.

str1 = "Hello"
str2 = "World"

# 1. string + string -> works (concatenation)
result_add = str1 + str2
print("string + string:", result_add, "-> Works")

# 2. string - string -> does NOT work
try:
    result_sub = str1 - str2
    print("string - string:", result_sub, "-> Works")
except TypeError as e:
    print("string - string -> Error:", e)

# 3. string * integer -> works (repetition)
result_mul = str1 * 3
print("string * integer:", result_mul, "-> Works")

# 4. string / string -> does NOT work
try:
    result_div = str1 / str2
    print("string / string:", result_div, "-> Works")
except TypeError as e:
    print("string / string -> Error:", e)

# Summary:
# Works:     string + string (concatenation), string * integer (repetition)
# Error:     string - string, string / string  -> both raise TypeError,
#            since subtraction and division have no defined meaning for strings.
