num = int(input("Enter the number: "))

num = str(num)

# if num == num[::-1]:
#     print("true")
# else:
#     print("false")

j = len(num)-1
i = 0
while j > i:
    if num[i] != num[j]:
        print("Not a palindrome")
        break
    i += 1
    j -= 1
else:
    print("It is a palindrome")