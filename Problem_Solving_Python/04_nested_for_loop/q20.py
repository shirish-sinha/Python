n = int(input("Enter the number: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print("SPECIAL", end=" ")
        elif i + j == n:
            print("PAIR", end=" ")
        else:
            print("NORMAL", end=" ")
    print()