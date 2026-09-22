num = int(input("Please enter a number: "))

if num % 11 == 0 and num % 5 == 0:
    print("It is divisible by both")
elif num % 11 == 0:
    print("Divisble by 11")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Divisible by none")