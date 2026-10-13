string = "1243asbhdcHJD+-  23"
up = 0
low = 0
space = 0
dig = 0
spec = 0

for i in range(len(string)):
    if "A" <= string[i] <= "Z":
        up += 1
    elif "a" <= string[i] <= "z":
        low += 1
    elif "0" <= string[i] <= "9":
        dig += 1
    elif string[i] == " ":
        space += 1
    else:
        spec += 1

if up == low or up == space or up == dig or up == spec or low == space or low == dig or low == spec or space == dig or space == spec:
    print("Tie")
elif up > low and up > space and up > dig and up > spec:
    print(f"Uppercase: {up}")
elif low > up and low > space and low > dig and low > spec:
    print(f"Lowercase: {low}")
elif space > up and low < space and space > dig and space > spec:
    print(f"Space: {space}")
elif dig > up and dig > space and space < dig and dig > spec:
    print(f"Digit: {dig}")
elif spec > low and spec > space and spec > dig and up < spec:
    print(f"Special: {spec}")