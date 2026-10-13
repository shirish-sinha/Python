junior = 0
mid = 0
senior = 0
executive = 0
total = 0
for i in range(8):
    salary = int(input("Enter your salary: "))
    if salary < 25000:
        junior += 1
        print("Junior")
    elif salary <= 50000:
        mid += 1
        print("Mid")
    elif salary < 100000:
        senior += 1
        print("Senior")
    else:
        executive += 1
        print("Executive")
    total += salary
print(f"Average: {total/8}")