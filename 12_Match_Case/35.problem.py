# Problem 35

print("1 : Starters")
print("2 : Main Course")
print("3 : Desserts")
print("4 : Drinks")

category = int(input("Enter category: "))

match category:
    case 1:
        print("1 : Soup")
        print("2 : Spring Roll")
        print("3 : Garlic Bread")
        item = int(input("Enter item: "))

        match item:
            case 1:
                print("Soup Selected")
            case 2:
                print("Spring Roll Selected")
            case 3:
                print("Garlic Bread Selected")
            case _:
                print("Invalid Item")

    case 2:
        print("1 : Pizza")
        print("2 : Pasta")
        print("3 : Biryani")
        item = int(input("Enter item: "))

        match item:
            case 1:
                print("Pizza Selected")
            case 2:
                print("Pasta Selected")
            case 3:
                print("Biryani Selected")
            case _:
                print("Invalid Item")

    case 3:
        print("1 : Ice Cream")
        print("2 : Cake")
        print("3 : Gulab Jamun")
        item = int(input("Enter item: "))

        match item:
            case 1:
                print("Ice Cream Selected")
            case 2:
                print("Cake Selected")
            case 3:
                print("Gulab Jamun Selected")
            case _:
                print("Invalid Item")

    case 4:
        print("1 : Coffee")
        print("2 : Tea")
        print("3 : Juice")
        item = int(input("Enter item: "))

        match item:
            case 1:
                print("Coffee Selected")
            case 2:
                print("Tea Selected")
            case 3:
                print("Juice Selected")
            case _:
                print("Invalid Item")

    case _:
        print("Invalid Category")