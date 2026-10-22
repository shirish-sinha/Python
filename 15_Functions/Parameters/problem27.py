def compare(a, b):
    if a > b:
        result = "A is greater"
    elif b > a:
        result = "B is greater"
    else:
        result = "Equal"

    difference = a - b if a >= b else b - a
    return result, difference


print(compare(8, 3))
print(compare(3, 8))
print(compare(5, 5))
