even_highest = 0
highest_num = 0
tied_nums = ""
for i in range(10):
    even = 0
    odd = 0
    num = int(input("Enter a number: "))
    num = str(num)
    for digit in num:
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1
    if even > even_highest:
        even_highest = even
        highest_num = num
    elif even == even_highest:
        tied_nums += num
        tied_nums += " "
        tied_nums += highest_num
print(highest_num)
print(tied_nums)