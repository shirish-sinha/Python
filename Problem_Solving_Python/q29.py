first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

if first == second or second == third or first == third:
    print("Please enter three different numbers.")
elif (first > second and first < third) or (first < second and first > third):
    print(first)
elif (second > first and second < third) or (second < first and second > third):
    print(second)
else:
    print(third)