age = int(input("Enter your age: "))

while not 0 <= age <= 120:
    print("You did not enter a valid age")
    age = int(input("Enter a valid age: "))
print(age)