# Problem 27

print("1 : General Medicine")
print("2 : Cardiology")
print("3 : Orthopedics")
print("4 : Pediatrics")
print("5 : Emergency")

choice = int(input("Enter department: "))

match choice:
    case 1:
        print("General Medicine Selected")
    case 2:
        print("Cardiology Selected")
    case 3:
        print("Orthopedics Selected")
    case 4:
        print("Pediatrics Selected")
    case 5:
        print("Emergency Selected")
    case _:
        print("Invalid Department")