limit = int(input("Enter n: "))
number = 1
even_count = 0
while number <= limit:
    if number % 2 == 0:
        even_count += 1
    number += 1
print("Count of even numbers:", even_count)