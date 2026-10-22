word = input("Enter a word: ")
word2 = input("Enter another word: ")
checked = ""
for i in range(len(word)):
    if word[i] not in checked:
        for j in range(len(word)):
            if word[i] == word2[j]:
                print(word[i])
                break
            else:
                continue
        checked += word[i]