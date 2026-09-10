char = input("Enter a character: ").lower()

if char >= "a" and char <= "z":
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid Input")