# Problem 26

print("1 : Light")
print("2 : Fan")
print("3 : AC")
print("4 : TV")

choice = int(input("Enter device: "))

match choice:
    case 1:
        print("Light Controller Opened")
    case 2:
        print("Fan Controller Opened")
    case 3:
        print("AC Controller Opened")
    case 4:
        print("TV Controller Opened")
    case _:
        print("Invalid Device")