def total(n):
    if n == 0:                  # Base Case
        return 0

    return n + total(n - 1)