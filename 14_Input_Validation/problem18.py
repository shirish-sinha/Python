month = int(input("Enter a month number: "))
day = int(input("Enter a day number: "))

while (not 1 <= day <= 31) or not (1 <= month <= 12):
    print("Invalid input")
    month = int(input("Enter a month number: "))
    day = int(input("Enter a day number: "))