highestscorer = ""
highscore = 0
for i in range(5):
    vowels = 0
    consonants = 0
    name = input("Enter your name: ").lower()
    marks = int(input("Enter your marks: "))
    if highscore < marks:
        highscore = marks
        highestscorer = name

    for char in name:
        if char == "a" or char == "e" or char == "i" or char == "u":
            vowels += 1
        else:
            consonants += 1
    print("Vowels: ", vowels)
    print("Consonants: ", consonants)
    print("Characters: ", len(name))
    if vowels > consonants:
        print("Vowel Heavy")
    else:
        print("Consonant Heavy")
print(f"Highest scorer: {highestscorer}")
print(f"Score: {highscore}")