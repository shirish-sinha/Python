sum = 0
num = int(input("Enter the number: "))

num = str(num)

for digit in num:
    if digit == "-":
        continue
    sum += int(digit)
print(sum)