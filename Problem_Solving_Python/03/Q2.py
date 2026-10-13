fail = 0
passed = 0
good = 0
excel = 0

for i in range(10):
    marks = int(input("Enter your marks: "))
    if marks < 35:
        print("Fail")
        fail += 1
    elif marks < 50:
        print("Pass")
        passed += 1
    elif marks < 75:
            print("Good")
            good += 1
    elif marks < 100:
            print("Excellent")
            excel += 1

print(f"Fail: {fail}")
print(f"Pass: {passed}")
print(f"Good: {good}")
print(f"Excellent: {excel}")