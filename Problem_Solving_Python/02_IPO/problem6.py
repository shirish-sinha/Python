
# IPO Model
# Input   : marks1, marks2, marks3
# Process : average = (marks1 + marks2 + marks3) / 3
#           check if average >= 40
# Output  : print Pass or Fail

# Dry Run
# case 1:
#   marks1 = 50, marks2 = 60, marks3 = 45
#   average = (50 + 60 + 45) / 3 = 155 / 3 = 51.67
#   51.67 >= 40 : True
#   Output: Pass
#
# Test case 2:
#   marks1 = 30, marks2 = 25, marks3 = 20
#   average = (30 + 25 + 20) / 3 = 75 / 3 = 25.0
#   25.0 >= 40 -> False
#   Output: Fail

marks1 = float(input("Enter marks of subject 1: "))
marks2 = float(input("Enter marks of subject 2: "))
marks3 = float(input("Enter marks of subject 3: "))

average = (marks1 + marks2 + marks3) / 3

if average >= 40:
    print("Pass")
else:
    print("Fail")
