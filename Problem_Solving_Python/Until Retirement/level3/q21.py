count = 0
num = int(input("Enter the number: "))

num = str(num)

for digit in num:
    if digit == "-":
        continue
    count += 1
print(count)