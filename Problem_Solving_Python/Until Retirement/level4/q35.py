str = input("Enter the string: ").lower()
uper = ""

for ch in str:
    if "a" <= ch <= "z":
        uper += chr(ord(ch) - 32)
    else:
        uper += ch

print(uper)