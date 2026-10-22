word = input("Enter a word: ")

for char in word:
    for chr in word:
        if chr == char:
            print(f"{chr}/{char} is same")
        else:
            print(f"{chr}/{char} is different")