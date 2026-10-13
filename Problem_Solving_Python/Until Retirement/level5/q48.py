str = input("Enter a string: ")
no_vowels = ""

for char in str:
    if char in "aeiouAEIOU":
        continue
    else:
        no_vowels += char
print(no_vowels)