# String compression counter:

string = input("Enter the string: ")
current = ""
output = ""
times = 0
for char in string:
    if char != current:
        output += str(times)
        current = char
        output += char
        times = 1
    elif char == current:
        times += 1
output += str(times)
print(output[1::])