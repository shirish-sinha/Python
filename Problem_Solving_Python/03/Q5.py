short = 0
med = 0
long = 0

sentence = input("Enter a sentence: ")
wordlist = sentence.split()

for word in wordlist:
    l = len(word)
    print(f"Length of the word is {l}")
    if l <= 3:
        print("Short")
        short += 1
    elif l <= 6:
        print("Medium")
        med += 1
    else:
        print("Long")
        long += 1

print(short)
print(med)
print(long)