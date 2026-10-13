# Problem 25

print("1 : Regular")
print("2 : Premium")
print("3 : VIP")

ticket_type = int(input("Enter ticket type: "))
age = int(input("Enter your age: "))

match ticket_type:
    case 1:
        if age <= 5:
            print("Free Ticket")
        else:
            print("Your selected ticket type is", ticket_type)
    case 2:
        if age <= 5:
            print("Free Ticket")
        else:
            print("Your selected ticket type is", ticket_type)
    case 3:
        if age <= 5:
            print("Free Ticket")
        else:
            print("Your selected ticket type is", ticket_type)
    case _:
        print("Invalid ticket type")
