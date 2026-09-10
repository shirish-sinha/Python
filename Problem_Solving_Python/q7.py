num = int(input("Please enter a number: "))

if num % 7 == 0 and num % 3 == 0:
    print("It is divisible by both")
elif num % 7 == 0:
    print("Divisble by 11")
elif num % 3 == 0:
    print("Divisible by 5")
else:
    print("Divisible by none")