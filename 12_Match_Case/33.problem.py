# Problem 33

print("1 : Flight")
print("2 : Train")
print("3 : Bus")

transport = int(input("Enter transport: "))

match transport:
    case 1:
        print("1 : Economy")
        print("2 : Business")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Economy Selected")
            case 2:
                print("Business Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("1 : Sleeper")
        print("2 : AC")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Sleeper Selected")
            case 2:
                print("AC Selected")
            case _:
                print("Invalid Option")

    case 3:
        print("1 : Ordinary")
        print("2 : Volvo")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Ordinary Selected")
            case 2:
                print("Volvo Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Transport")