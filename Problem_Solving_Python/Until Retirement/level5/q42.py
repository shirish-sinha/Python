word = input("Enter a string: ")
with_e = ""

for chr in word:
    if chr == "A":
        with_e += "E"
    elif chr == "a":
        with_e += "e"
    else:
        with_e += chr
print(with_e)