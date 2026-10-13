# Problem 15

print("1 : Bronze")
print("2 : Silver")
print("3 : Gold")
print("4 : Platinum")
numb = int(input("Enter Your Membership Level: "))

match numb:
    case 1 | 2:
        print("Basic Membership")
    case 3 | 4:
        print("Premium Membership")
    case _:
        print("Unknown Membership Level")
