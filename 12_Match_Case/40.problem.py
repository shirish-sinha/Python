# Problem 40

menu=int(input("""
                   1 for Student:-
                   2 for Teacher:-
                   3 for Administration
                     ENTER:-"""))

match menu:
    case 1:
        print("Student")
        stu=int(input("""
                         1 for Profile
                         2 for Marks
                         3 for Attendancw
                         4 for courses
                         ENTER:-"""))
        match stu:
            case 1:
                print("Profile")
            case 2:
                print("marks")
            case 3:
                print("Attendence")
            case 4:
                print("Cources")
            case _:
                print("INVALID INPUT")
    case 2:
            print("teacher")
            stu=int(input("""
                             1 for Student
                             2 for enter Marks
                             3 for Attendancw
                             4 for courses
                             ENTER:-"""))
            match stu:
                case 1:
                    print("Student")
                case 2:
                    print("enter marks")
                case 3:
                    print("Attendence")
                case 4:
                    print("Cources")
                case _:
                    print("INVALID INPUT")
    
