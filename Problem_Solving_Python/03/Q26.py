poor = 0
avg = 0
good = 0
excel = 0
outstanding = 0
sum = 0
for i in range(10):
    rating = float(input("Enter a rating: "))
    if rating < 0:
        print("Enter a valid rating")
    elif rating < 3:
        poor += 1
        print("Poor")
    elif rating < 5:
        avg +=1
        print("Average")
    elif rating < 7:
        good += 1
        print("Good")
    elif rating < 9:
        excel += 1
        print("Excellent")
    else:
        outstanding += 1
        print("Outstanding")

    sum += rating

print(f"Average: {sum/10}")