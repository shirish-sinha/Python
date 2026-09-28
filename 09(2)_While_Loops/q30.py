i = 1
j = int(input("Enter the size of the grid: "))
while i <= j:
    number = 1
    while number <= j:
        print(i *  number, end="\t")
        number += 1
    print()
    i += 1