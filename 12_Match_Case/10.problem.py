# Problem 10

print(" 1 : UPI  2 : Card 3 : Cash 4 : Wallet")
numb = int(input("Enter your Payment method: "))

match numb:
    case 1:
        print("UPI Payment selected")
    case 2:
        print("Card Payment selected")
    case 3:
        print("Cash Payment selected")
    case 4:
        print("Wallet Payment selected")
    case _:
        print("Invalid Payment method ")

