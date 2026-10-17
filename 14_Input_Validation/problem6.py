temp = int(input("Enter the temperature: "))

while not -20 <= temp <= 45:
    print("You did not enter a valid temperature")
    temp = int(input("Enter a valid temperature: "))
print(temp)