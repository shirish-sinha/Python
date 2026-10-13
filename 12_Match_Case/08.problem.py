# Problem 8

numb = 1
while numb != 5:

    print(" 1 : Morning Show 2 : Afternoon Show  3 : Evening Show 4 : Nigth Show 5 : Exit")

    numb = int(input("Enter your choice: "))

    match numb:
        case 1:
            print("Morning Show Details are as follows:")
        case 2:
            print("Afternoon Show Details are as follows:")
        case 3:
            print("Evening Show Details are as follows:")
        case 4:
            print("Night Show Details are as follows:")
        case 5:
            print("Exited!")
        case _ :
            print("Invalid Input")
