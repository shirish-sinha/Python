str = input("Enter the string: ")
swap = ""

for ch in str:
    if "A" <= ch <= "Z":
        swap += chr(ord(ch) + 32)
    elif "a" <= ch <= "z":
        swap += chr(ord(ch) - 32)
    else:
        swap += ch

print(swap)