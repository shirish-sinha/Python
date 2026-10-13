# Problem 22

print("1 : Kilometers to meters")
print("2 : Meters to Kilometers")
print("3 : Kilograms to Grams")
print("4 : Grams to Kilograms")

choice = int(input("Enter your choice number: "))
num = int(input("Enter your value: "))

match choice:
    case 1:
        meters = num * 1000
        print(f"{num} kms is equal to {meters} meters")
    case 2:
        kilometers = num / 1000
        print(f"{num} meters is equal to {kilometers} kms")
    case 3:
        grams = num * 1000
        print(f"{num} kilograms is equal to {grams} grams.")
    case 4:
        kilograms = num / 1000
        print(f"{num} grams is equal to {kilograms} kgs.")
    case _:
        print("Invalid choice number")
