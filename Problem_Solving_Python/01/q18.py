temp = int(input("Enter a temperature (In celsius): "))

if temp < 0:
    print("Freezing")
elif temp <= 15:
    print("Very cold")
elif temp <= 25:
    print("Cold")
elif temp <= 35:
    print("Normal")
else:
    print("Hot")