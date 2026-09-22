day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

if 0 < day <= 31 and 0 < month <= 12 and year > 0:
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            print("The date is invalid")
        else:
            print("The date is valid")
    elif month == 2:
        if (year % 400 == 0 or (year % 4 == 0 and year % 10 != 0)) and day <= 29:
            print("The date is valid")
            print(f"Date: {day}/{month}/{year}")
        elif day <= 28:
            print("The date is valid")
            print(f"Date: {day}/{month}/{year}")
        else:
            print("The date is invalid")
    else:
        print("The date is valid")
        print(f"Date: {day}/{month}/{year}")
else:
    print("The date is invalid")