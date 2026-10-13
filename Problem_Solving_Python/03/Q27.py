sentence = input("Enter a sentence: ").lower().split()
current = ""
words_repeated = ""
for i in range(len(sentence)):
    if sentence[i] != current:
        current = sentence[i]
        for j in range(i + 1, len(sentence)):
            if sentence[j] == current and sentence[i] not in words_repeated.split():
                words_repeated += sentence[i]
                words_repeated += " "
            else:
                continue
print(words_repeated)