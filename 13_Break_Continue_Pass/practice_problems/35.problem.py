while True:
    n = int(input("Enter a number: "))
    if n > 0:
        print(n)
    elif n < 0:
        continue
    else:
        break

numbers = [12, 5, -4, 18, 0, 25, 30]
for i in numbers:
    if i < 0:
        continue
    if i == 0:
        break
    print(i)

numbers = [10, 20, 30, 40]
search = 30
found = False
for i in numbers:
    if i == search:
        found = True
        print("Number found")
        break
if not found:
    print("Number not found")
