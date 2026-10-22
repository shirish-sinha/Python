word = input("Enter a word: ")
checked = ""
for i in range(len(word)):
    count = 1
    if word[i] not in checked:
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                count += 1
            else:
                continue
        print(f"{word[i]} = {count}")
    checked += word[i]