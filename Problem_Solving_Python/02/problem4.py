
# IPO Model
# Input   : age
# Process : check if age is greater than or equal to 18
# Output  : print whether the person is eligible to vote

# Dry Run
# case 1:
#   age = 20
#   20 >= 18 : True
#   Output: Eligible to vote
#
# case 2:
#   age = 15
#   15 >= 18 : False
#   Output: Not eligible to vote

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
