# Problem 24

print("1 : Start Exam")
print("2 : View Result")
print("3 : Exit")
choice = int(input("Enter your choice Number: "))
age = int(input("Enter your age: "))

match choice:
    case 1:
        if age >= 18:
            print("You can start the exam")
        else:
            print("You are under threshold age")
    case 2:
        print("You can see your result")
    case 3:
        print("Exam ended")
    case _:
        print("Invalid choice number")
