# Problem 19

category = int(input("Enter category: "))
food = int(input("Enter food: "))

match category:
    case 1:
        match food:
            case 1:
                print("Paneer Selected")
            case 2:
                print("Dal Selected")
            case 3:
                print("Veg Biryani Selected")

    case 2:
        match food:
            case 1:
                print("Chicken Biryani Selected")
            case 2:
                print("Chicken Curry Selected")
            case 3:
                print("Fish Fry Selected")

    case _:
        print("Invalid Category")