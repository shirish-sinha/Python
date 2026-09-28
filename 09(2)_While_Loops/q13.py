limit = int(input("Enter n: "))
number = 1
while number <= limit:
    if number % 3 == 0:
        print(number)
    number += 1