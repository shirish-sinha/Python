n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        num = i * j
        if num % 5 == 0:
            print("F")
        if num % 2 == 0:
            print("E")
        else:
            print("O")