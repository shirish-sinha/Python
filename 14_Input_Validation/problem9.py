num = int(input("Enter a number divisible by 3 & 5: "))

while not num % 15 == 0:
    num = int(input("Enter a number divisible by 3 & 5: "))
print(num)