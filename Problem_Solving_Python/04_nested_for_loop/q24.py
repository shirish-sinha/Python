word = input("Enter a word: ")
word2 = input("Enter another word: ")

for char in word:
    for chr in word2:
        if chr == char:
            print(f"{chr}{char}", end=" ")
            print()