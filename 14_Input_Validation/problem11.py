num = int(input("Enter a number between 10 and 50 (inclusive): "))

while not 10 <= num <= 50:
    num = int(input("Enter a valid number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
