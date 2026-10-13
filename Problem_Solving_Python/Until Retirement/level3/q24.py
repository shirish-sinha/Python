rev = ""
num = int(input("Enter the number: "))

num = str(num)

for digit in range(len(num)-1, -1, -1):
    if num[0] == "-" and "-" not in rev:
        rev += "-"
    rev += num[digit]

if rev[len(num)] == "-":
    print(rev[:len(num)])
else:
    print(rev)