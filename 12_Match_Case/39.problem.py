# Problem 39

menu=int(input("""Enter:
      1 for Employee
      2 for manager:
                   
                   """))

match menu:
    case 1:
        print("Employee:-")
        option=int(input("""Enter:-
                             1 for View profile:-
                             2 for Apply leave:-
                             3 for View salary:-"""))
        match option:
            case 1:
                print("Profile")
            case 2 :
                leave=int(input("Enter total days of leave:-"))
                if leave>0 and leave<5:
                    print("Leave Granted")
                else:
                    print("Invalid leave")
            case 3:
                print("Salary")
            case _:
                print("INVALID INPUT")
    case 2:
        print("Manager:-")
        opt=int(input("""Enter:-
                             1 for View Team:-
                             2 for Approve leave:-
                             3 for View report:-"""))
        match opt:
            case 1:
                print("view Team:-")
            case 2:
                print("Approve leave")
            case 3:
                print("View report")
            case _:
                print("INVALID INPUT")
    case _:
        print("INVALID INPUT")
