word = input("Enter a word: ")

for char in word:
    for chr in word:
        if chr != char:
            print(char,chr)