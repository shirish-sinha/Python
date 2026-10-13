string = input("Enter a string: ")
up = 0
low = 0
dig = 0
spec = 0

for char in string:
    if "A" <= char <= "Z":
        up += 1
    elif "a" <= char <= "z":
        low += 1
    elif "0" <= char <= "9":
        dig += 1
    else:
        spec += 1

print(f"Uppercase%: {(up/len(string))*100}%")
print(f"Lowercase%: {(low/len(string))*100}%")
print(f"Digit%: {(dig/len(string))*100}%")
print(f"Special%: {(spec/len(string))*100}")

if up > low and up > dig and up > spec:
    print("Uppercase Heavy")
elif up < low and low > dig and low > spec:
    print("Lowercase Heavy")
elif dig > low and up < dig and dig > spec:
    print("Digit Heavy")
else:
    print("Special Character heavy")