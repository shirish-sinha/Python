# Problem 2

choice=int(input("""Enter:
                    1 for Wi-Fi:
                    2 for Bluetooth
                    3 for mobile data
                    4 for Airplane mode
                    5 for Exit:
                    
                    """))

match choice:
    case 1:
        print("Wi-Fi")
    case 2:
        print("Bluetooth")
    case 3:
        print("Mobile Data")
    case 4:
        print("Airplane Mode")
    case 5 :
        print("Exit")
    case _:
        print("Invalid input")