print("1 : Electronics \n2 : Clothing\n3 : Books\n4 : Grocery\n5 : Exit")
numb = int(input("Enter your choice: "))

match numb:
    case 1:
        print("Electronics")
    case 2:
        print("Clothing")
    case 3:
        print("Books")
    case 4:
        print("Grocery")
    case 5:
        print("Exited!")
