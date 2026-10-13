string = input("Enter the string: ")

length = len(string)
rev = ""
for i in range(length - 1, -1, -1):
    rev += string[i]

print(rev)