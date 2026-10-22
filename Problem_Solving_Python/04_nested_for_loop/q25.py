word = input("Enter a word: ")
word2 = input("Enter another word: ")
count = 0
for char in word:
    for chr in word2:
        if chr == char:
            count += 1

print(count)