# Problem 38

print("1: Engine")
print("2: Lights")
print("3: Music")
print("4: Navigation")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("1: Start")
        print("2: Stop")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Engine Started")
            case 2:
                print("Engine Stopped")
            case _:
                print("Invalid Option")

    case 2:
        print("1: Headlights")
        print("2: Indicators")
        print("3: Hazard Lights")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Headlights Selected")
            case 2:
                print("Indicators Selected")
            case 3:
                print("Hazard Lights Selected")
            case _:
                print("Invalid Option")

    case 3:
        print("1: Play")
        print("2: Pause")
        print("3: Next")
        print("4: Previous")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Music Playing")
            case 2:
                print("Music Paused")
            case 3:
                print("Next Song")
            case 4:
                print("Previous Song")
            case _:
                print("Invalid Option")

    case 4:
        print("1: Start Navigation")
        print("2: Stop Navigation")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Navigation Started")
            case 2:
                print("Navigation Stopped")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Choice")