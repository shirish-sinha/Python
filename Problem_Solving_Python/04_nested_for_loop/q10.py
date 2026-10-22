n = int(input("Enter the number: "))

for i in range(n):
    for j in range(n):
        print(j%2, end="")
    print()