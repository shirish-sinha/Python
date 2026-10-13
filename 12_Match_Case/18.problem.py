# Problem 18

category = input("Enter your category: ").strip().lower()
choice = int(input("Enter your choice number: "))

match category:
    case "electronics":
        match choice:
            case 1:
                print("Mobile")
            case 2:
                print("Laptop")
            case 3:
                print("Headphones")
    case "clothing":
        match choice:
            case 1:
                print("Shirt")
            case 2:
                print("Jeans")
            case 3:
                print("Shoes")
    case _:
        print("Invalid category")