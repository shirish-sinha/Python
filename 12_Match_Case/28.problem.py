# Problem 28

print("1 : Book Ticket")
print("2 : Cancel Ticket")
print("3 : Check PNR")
print("4 : Train Schedule")
print("5 : Exit")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Book Ticket Selected")
    case 2:
        print("Cancel Ticket Selected")
    case 3:
        print("Check PNR Selected")
    case 4:
        print("Train Schedule Selected")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")