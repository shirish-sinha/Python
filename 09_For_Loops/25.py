s = input("Enter a string: ")
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 0
for ch in s:
    for letter in uppercase_letters:
        if ch == letter:
            count = count + 1
print(count)
