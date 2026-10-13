even = 0
odd = 0
positive = 0
negative = 0
zero = 0
largest = 0

for i in range(3):
    for j in range(3):
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1
        if largest < num:
            largest = num

print(f"Even: {even}; Odd {odd}; Positive: {positive}; Negative {negative}; Zero: {zero}; Largest Number: {largest}")
