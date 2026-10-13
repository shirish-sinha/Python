# Problem 34
print("1 : Start Game")
print("2 : Load Game")
print("3 : Settings")
print("4 : Exit")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Game Started")

    case 2:
        print("Game Loaded")

    case 3:
        print("1 : Sound")
        print("2 : Graphics")
        print("3 : Controls")
        option = int(input("Enter setting: "))

        match option:
            case 1:
                print("Sound Settings Opened")
            case 2:
                print("Graphics Settings Opened")
            case 3:
                print("Controls Settings Opened")
            case _:
                print("Invalid Setting")

    case 4:
        print("Exit")

    case _:
        print("Invalid Choice")