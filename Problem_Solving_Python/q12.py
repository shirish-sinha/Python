char = input("Enter a character")

if char >= "A" and char <= "Z":
    print("Uppercase Alphabet")
elif char >= "a" and char <= "z":
    print("Lowercase Character")
elif char >= "0" and char <= "9":
    print("Digit")
else:
    print("Special Character")