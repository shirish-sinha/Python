sent = input("Enter a sentence: ").lower().split()

for word in sent:
    vowels = 0
    consonants = 0
    for char in word:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            vowels += 1
        elif "a" <= char <= "z":
            consonants += 1
    print(word)

    if vowels > consonants:
        print("Vowel heavy")
    elif consonants > vowels:
        print("Consonant heavy")
    else:
        print("Balanced")