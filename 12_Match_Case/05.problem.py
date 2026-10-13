# Problem 5

choice=int(input("""Enter:
      1: View Profile
      2: View Courses
      3: View Marks
      4: View Attendance
      5: Logout:        
                    """))

match choice:
    case 1:
        print("prifile")
    case 2:
        print("courses")
    case 3:
        print("marks")
    case 4:
        print("attendence")
    case 5 :
        print("Logout")
    case _:
        print("Invalid input")
