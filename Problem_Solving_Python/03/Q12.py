vowels = 0
consonants = 0
a = 0
e = 0
i = 0
o = 0
u = 0

sent = input("Enter a sentence: ").lower()

for char in sent:
    if char == "a": 
        vowels += 1
        a += 1
    elif char == "e":
        vowels += 1
        e += 1
    elif char == "i":
        vowels += 1
        i += 1
    elif char == "o":
        vowels += 1
        o += 1
    elif char == "u":
        vowels += 1
        u += 1
    elif "a" <= char <= "z":
        consonants += 1
    else:
        print("Please enter a sentence without numbers")
        break

if vowels > consonants:
    print("Vowels win")
elif consonants > vowels:
    print("Consonants win")
else:
    print("Draw")
print(f"a: {a}; e: {e}; i: {i}; o: {o}; u: {u}")