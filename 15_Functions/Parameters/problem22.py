def calculate_stats(a, b, c):
    return min(a, b, c), max(a, b, c), a + b + c


print(calculate_stats(8, 3, 5))
