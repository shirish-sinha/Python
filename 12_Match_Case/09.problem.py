# Problem 9

print(" 1 : Sunny  2 : Rainy 3 : Cloudy 4 : Snowy")
numb = int(input("Enter your Weather: "))

match numb:
    case 1:
        print("Wear Sunglasses")
    case 2:
        print("Carry an Umbrella")
    case 3:
        print("Weather may Change")
    case 4:
        print("Wear warm clothes")
    case _:
        print("Unkown Weather")
