# Problem 23

Account_type = input("Enter your account type: ").strip().lower()
amount = int(input("Enter your amount: "))

match Account_type:
    case "savings":
        if amount > 0:
            print("Withdrawal Request Accepted")
        else:
            print("Invalid amount")
    case "current":
        if amount > 0:
            print("Withdrawal request Accepted")
        else:
            print("Invalid Amount")
    case _:
        print("Invalid Account Type")