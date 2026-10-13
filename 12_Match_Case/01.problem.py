# Problem 1

choice=int(input("""Enter:
                    1 for pizza:
                    2 for burger
                    3 for pasta
                    4 for sandwitch:
                    
                    """))

match choice:
    case 1:
        print("Pizza")
    case 2:
        print("Burger")
    case 3:
        print("Pasta")
    case 4:
        print("sandwitch")
    case _:
        print("Invalid input")