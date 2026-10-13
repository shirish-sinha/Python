# Problem 36

print("1: UPI")
print("2: Card")
print("3: Wallet")

payment = int(input("Enter payment type: "))

match payment:
    case 1:
        print("1: Scan QR")
        print("2: Enter UPI ID")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Scan QR Selected")
            case 2:
                print("Enter UPI ID Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("1: Credit Card")
        print("2: Debit Card")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Credit Card Selected")
            case 2:
                print("Debit Card Selected")
            case _:
                print("Invalid Option")

    case 3:
        print("1: Add Money")
        print("2: Pay Using Wallet")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Add Money Selected")
            case 2:
                print("Pay Using Wallet Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Payment Type")