failed = 0
highest = 0
lowest = 100
for i in range(5):
    total = 0
    name = input("Enter student name: ")
    for j in range(5):
        marks = int(input("Enter marks: "))
        total += marks
        if marks >= 35:
            if marks < 50:
                print(f"Grade: C")
            elif marks < 75:
                print(f"Grade: B")
            elif marks < 100:
                print(f"Grade: A")
        else:
            print(f"Grade: F")
    percent = total/5
    if percent < 35:
        failed += 1
    if percent > highest:
        highest = percent
    if percent < lowest:
        lowest = percent

print(f"Passed students: {5 - failed}")
print(f"Failed students: {failed}")
print(f"Highest percentage: {highest}")
print(f"Lowest percentage: {lowest}")