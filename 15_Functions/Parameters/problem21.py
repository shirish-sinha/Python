def analyze_number(number):
    if number % 2 == 0:
        is_even = "even"
    else:
        is_even = "odd"
    if number >= 0:
        absolute = number
    else:
        absolute = -number
    digit_count = len(str(absolute))
    return f"The number: {number} has {digit_count} digits, is {is_even} and has an absolute value of {absolute}"


print(analyze_number(-246))
