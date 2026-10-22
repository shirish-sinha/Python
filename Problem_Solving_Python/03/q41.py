for i in range(7):
    count = 0
    for j in range(5):
        present = input("Enter 'P' if present any other character if absent: ").lower()

        if present == "p":
            count += 1

    percent = count * 20

    if percent > 90:
        print(f"Attendence: {percent}% \n Excellent")
    elif percent > 75:
        print(f"Attendence: {percent}% \n Good")
    else:
        print(f"Attendence: {percent}% \n Warning")