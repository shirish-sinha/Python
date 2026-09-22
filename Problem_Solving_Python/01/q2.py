num = int(input("Enter an integer: "))

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
if num < 0:
    if num % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")
else:
    print("Zero")