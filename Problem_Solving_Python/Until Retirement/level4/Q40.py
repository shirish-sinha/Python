string = input("Enter a string: ")
no_space = ""

for char in string:
    if char != " ":
        no_space += char

print(no_space)