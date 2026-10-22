word = input("Enter a word: ")

for char in word:
    for i in range(3):
        print(char, end="")
    print()