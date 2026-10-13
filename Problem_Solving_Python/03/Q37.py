word = input("Enter the word: ")

for i in range(len(word)):
    for j in range(i+1):
        print(word[j], end=" ")
    print()
for i in range(len(word)):
    for j in range(len(word)-i-1, -1, -1):
        print(word[j], end=" ")
    print()