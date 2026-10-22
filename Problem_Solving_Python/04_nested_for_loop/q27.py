word = input("Enter a word: ")
for char in word:
    for vowel in "AEIOUaeiou":
        if char == vowel:
            print(f"{char} = Vowel")
            break
    else:
        print(f"{char} = Consonant")