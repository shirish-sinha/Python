def max_digit(n):
    if n == 0:
        return 0
    a = max_digit(n//10)
    if n%10 > a:
        return n%10
    else:
        return a

print(max_digit(6475))