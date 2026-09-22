
# IPO Model
# Input   : price (price of the item entered by the user)
# Process : if price >= 2000, subtract 20% discount from price
# Output  : print the final price

# Dry Run
# case 1:
#   price = 2500
#   2500 >= 2000 : True
#   discount = 2500 * 20 / 100 = 500
#   final_price = 2500 - 500 = 2000
#   Output: 2000
#
# case 2:
#   price = 1500
#   1500 >= 2000 : False
#   final_price = 1500
#   Output: 1500

price = float(input("Enter the price of the item: "))

if price >= 2000:
    discount = price * 20 / 100
    final_price = price - discount
else:
    final_price = price

print("The final price is:", final_price)
