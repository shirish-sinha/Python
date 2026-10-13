# Problem 13

day_number = int(input("Enter the Day Number: "))

match day_number:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid Day")