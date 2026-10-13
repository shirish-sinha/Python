# Problem 21

print("1: Celsius to Fahrenheit")
print("2: Fahrenheit to Celsius")
choice = int(input("Enter your choice number: "))
temp = int(input("Enter your temperature: "))

match choice:
    case 1:
        fahrenheit = (temp * 9/5) + 32
        print(f"{temp}°C is equal to {fahrenheit}°F")

    case 2:
        celsius = (temp - 32) * 5/9
        print(f"{temp}°F is equal to {celsius}°C")

    case _:
        print("Invalid choice number")