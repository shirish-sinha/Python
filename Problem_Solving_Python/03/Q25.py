n = int(input("Enter the num: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j % 15 == 0:
            print("F", end=" ")
        elif j % 3 == 0:
            print("T", end=" ")
        elif j % 2 == 0:
            print("E", end=" ")
        else:
            print("O", end=" ")
    print()