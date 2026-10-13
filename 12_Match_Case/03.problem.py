# Problem 3

choice=int(input("""Enter:
                    1 for Check Balance-:
                    2 for Withdraw Money
                    3 for mobile data
                    4 for Airplane mode
                    5 for Exit:
                    
                    """))

match choice:
    case 1:
        print("Check Balance")
    case 2:
        print("Withdraw Money")
    case 3:
        print("Mobile Data")
    case 4:
        print("Airplane Mode")
    case 5 :
        print("Exit")
    case _:
        print("Invalid input")