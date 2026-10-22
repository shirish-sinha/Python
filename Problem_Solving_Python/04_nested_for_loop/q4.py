row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

for i in range(row):
    for j in range(col):
        print(f"({i},{j})", end=" ")
    print()