
# IPO Model
# Input   : num
# Process : check the remainder when num is divided by 2
# Output  : print Even or Odd

# Dry Run
# case 1:
#   num = 10
#   10 % 2 = 0 : True
#   Output: Even
#
# case 2:
#   num = 7
#   7 % 2 = 1 : False
#   Output: Odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
