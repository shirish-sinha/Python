product = 1
num = int(input("Enter the number: "))

num = str(num)

for digit in num:
    if digit == "-":
        continue
    product *= int(digit)
print(product)