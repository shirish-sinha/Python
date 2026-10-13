str = input("Enter a string: ")
no_digit = ""
for char in str:
    if char.isdigit():
        continue
    else:
        no_digit += char
print(no_digit)