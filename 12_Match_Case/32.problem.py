# Problem 32

print("1 : Student")
print("2 : Teacher")
print("3 : Parent")

role = int(input("Enter role: "))

match role:
    case 1:
        print("1 : Marks")
        print("2 : Attendance")
        print("3 : Homework")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Student Marks Selected")
            case 2:
                print("Student Attendance Selected")
            case 3:
                print("Student Homework Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("1 : Enter Marks")
        print("2 : Attendance")
        print("3 : Assign Homework")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Enter Marks Selected")
            case 2:
                print("Teacher Attendance Selected")
            case 3:
                print("Assign Homework Selected")
            case _:
                print("Invalid Option")

    case 3:
        print("1 : Child Marks")
        print("2 : Child Attendance")
        print("3 : Contact Teacher")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Child Marks Selected")
            case 2:
                print("Child Attendance Selected")
            case 3:
                print("Contact Teacher Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Role")