marks1 = int(input("Enter English marks: "))
marks2 = int(input("Enter Maths marks: "))
marks3 = int(input("Enter Science marks: "))

if 0 <= marks1 <= 100 and 0 <= marks2 <= 100 and 0 <= marks3 <= 100:
    if marks1 > 35 and marks2 > 35 and marks3 > 35:
        avg = (marks1 + marks2 + marks3)/3
        if avg >= 75:
            print("Distinction")
        elif avg >= 60:
            print("First Class")
        elif avg >= 50:
            print("Second Class")
        else:
            print("Pass")
    else:
        print("Fail")
else:
    print("Please enter valid marks")