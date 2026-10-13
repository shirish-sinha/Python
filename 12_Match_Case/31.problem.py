# Problem 31

print("1 : Personal Banking")
print("2 : Business Banking")

banking_type = int(input("Enter banking type: "))

match banking_type:
    case 1:
        print("1 : Balance")
        print("2 : Transfer")
        print("3 : Loan")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Personal Banking - Balance Selected")
            case 2:
                print("Personal Banking - Transfer Selected")
            case 3:
                print("Personal Banking - Loan Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("1 : Balance")
        print("2 : Payroll")
        print("3 : Business Loan")
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Business Banking - Balance Selected")
            case 2:
                print("Business Banking - Payroll Selected")
            case 3:
                print("Business Loan Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Banking Type")