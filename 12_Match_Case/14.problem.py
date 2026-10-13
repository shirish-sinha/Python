# Problem 14

print("1 : Low")
print("2 : Medium")
print("3 : High")
print("4 : Critical")
numb = int(input("Enter priority number: "))

match numb:
    case 1 | 2:
        print("Normal")
    case 3 | 4:
        print("Urgent")
    case _:
        print("Unknown Priority number")
