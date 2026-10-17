pin = 2568

attempt = int(input("Enter the pin: "))
attempts = 1

while attempts <= 3:
    if attempt == pin:
        print("Success")
        break
    else:
        print("Invalid pin")
        attempt = int(input("Enter the valid pin: "))
        attempts += 1
else:
    print("Device has been locked for 10 minutes")