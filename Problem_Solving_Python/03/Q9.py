string = input("Enter the string: ")
vowel = 0
consonant = 0
digit = 0
special = 0

for i in range(len(string)):
    if string[i] == " ":
        print("[space]")
    else:
        print(string[i])
    print(i)
    if i % 2 == 0:
        print("Even")
    else:
        print("Odd")
    if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u" or string[i] == "A" or string[i] == "E" or string[i] == "I" or string[i] == "O" or string[i] == "U":
        vowel += 1
        print("Vowel")
    elif "a" <= string[i] <= "z" or "A" <= string[i] <= "Z":
        consonant += 1
        print("Consonant")
    elif "0" <= string[i] <= "9":
        digit += 1
        print("Digit")
    else:
        special += 1
        print("Special Character")
    print()

print(f"Special Characters: {special}")
print(f"Digits: {digit}")
print(f"Consonants: {consonant}")
print(f"Vowels: {vowel}")