str = input("Enter the string: ").lower()
uper = ""

for ch in str:
    if "A" <= ch <= "B":
        uper += chr(ord(ch) + 32)
    else:
        uper += ch

print(uper)