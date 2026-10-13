# Problem 7

numb = 1
while numb != 6:

    print("1 :Account Balance 2 : Mini Statement  3 : Fund Transfer 4 : Bill Payment 5 : Customer Support 6 : Exit")

    numb = int(input("Enter your choice: "))

    match numb:
        case 1:
            print("Balance:")
        case 2:
            print("Mini Statement:")
        case 3:
            print("Fund Transfer:")
        case 4:
            print("Bill Payments")
        case 5:
            print("Customer Support")
        case 6:
            print("Exited!")
        case _ :
            print("Invalid Input")

