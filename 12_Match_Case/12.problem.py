# Problem 12

print("1 : Admin 2 : Teacher 3 : Student 4 : Guest")
numb = int(input("Enter your role: "))

match numb:
    case 1:
        print("Full Access")
    case 2:
        print("Teacher Dashboard")
    case 3:
        print("Student Dashboard")
    case 4:
        print("Limited Access")
    case _:
        print("Invalid input")

