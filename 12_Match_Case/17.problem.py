# Problem 17

account = input("Enter your account type: ").strip().lower()
choice = int(input("Enter your choice number: "))

match account:
    case "savings":
        match choice:
            case 1:
                print("Check Balance")
            case 2:
                print("Deposit")
            case 3:
                print("Withdraw")

    case "current":
        match choice:
            case 1:
                print("Check Balance")
            case 2:
                print("Deposit")
            case 3:
                print("Withdraw")

    case _:
        print("Invalid Account type")