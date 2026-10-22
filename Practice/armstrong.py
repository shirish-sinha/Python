limit = int(input("Enter the range: "))

for i in range(limit + 1):
    total = 0
    digits = len(str(i))
    for dig in str(i):
        total += int(dig) ** digits
    if total == i:
        print(i)