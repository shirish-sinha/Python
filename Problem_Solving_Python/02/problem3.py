
# IPO Model
# Input   : num1, num2, num3
# Process : compare the three numbers using if-else to find the largest
# Output  : print the largest number

# Dry Run
# case 1:
#   num1 = 4, num2 = 9, num3 = 7
#   num1 >= num2 : 4 >= 9 : False
#   num2 >= num1 : num2 >= num3 : 9 >= 4 and 9 >= 7 : True
#   largest = 9
#   Output: 9
#
# case 2:
#   num1 = 15, num2 = 15, num3 = 10
#   num1 >= num2 and num1 >= num3 : 15 >= 15 and 15 >= 10 : True
#   largest = 15
#   Output: 15

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is:", largest)
