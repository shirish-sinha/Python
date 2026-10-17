marks = int(input("Enter your marks: "))

while not 0 <= marks <= 100:
    print("Invalid marks")
    marks = int(input("Enter valid marks: "))
if marks < 35:
    print("Fail")
elif marks < 60:
    print("Pass")
elif marks < 75:
    print("First Class")
else:
    print("Distinction")