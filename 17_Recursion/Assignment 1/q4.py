def answer(n):
    if n == 0:
        return 0

    n + answer(n - 1)

print(answer(3))

# Gives type error because no return statement is written in the recursive case, so the function returns None. We cannot add None and int