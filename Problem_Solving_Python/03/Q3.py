wordlist = input("Enter a sentence: ").split()

points = 0
maxpoints = 0

for word in wordlist:
    for i in word:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            points += 2
        elif "a" <= i <= "z" or "A" <= i <= "Z":
            points += 1
        elif "0" <= i <= "9":
            points += 3
        else:
            points += 4
    if points > maxpoints:
        maxpoints = points
        maxword = word
    points = 0

print(f"Word with the highest score: {maxword} ; Score: {maxpoints}")