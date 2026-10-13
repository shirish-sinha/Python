# Problem 37

print("1: Programming")
print("2: Mathematics")
print("3: Communication")

subject = int(input("Enter subject: "))

match subject:
    case 1:
        print("1: Python")
        print("2: Java")
        print("3: C++")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Python Selected")
            case 2:
                print("Java Selected")
            case 3:
                print("C++ Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("1: Algebra")
        print("2: Calculus")
        print("3: Statistics")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Algebra Selected")
            case 2:
                print("Calculus Selected")
            case 3:
                print("Statistics Selected")
            case _:
                print("Invalid Option")

    case 3:
        print("1: English")
        print("2: Presentation")
        print("3: Interview Skills")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("English Selected")
            case 2:
                print("Presentation Selected")
            case 3:
                print("Interview Skills Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Subject")