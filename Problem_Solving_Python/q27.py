hrs = int(input("Enter the hours: "))
mins = int(input("Enter the minutes: "))
secs = int(input("Enter the seconds: "))

if 0 <= hrs <= 23 and 0 <= mins <= 59 and 0 <= secs <= 59:
    print("The time is valid")
    print(f"Time: {hrs}:{mins}:{secs}")
else:
    print("The time is invalid")