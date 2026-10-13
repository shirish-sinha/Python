sent = input("Enter a string: ").split()
word_count = 0
longest = ""
shortest = "daefvhehrfiueharfiucheauefbcukeabsdcbdbcuieqahscduihqeauidchdqiuasbcuiau9cu"
vowel_start = 0
vowel_end = 0
digit = 0
char_count = 0
for word in sent:
    word_count += 1
    if word[0].lower() in "aeiou":
        vowel_start += 1
    if word[-1].lower() in "aeiou":
        vowel_end += 1
    if len(longest) < len(word):
        longest = word
    if len(shortest) > len(word):
        shortest = word
    for chr in word:
        if not chr == " ":
            char_count += 1
        if chr in "0123456789":
            digit += 1
            break

print(f"The number of words is: {word_count}")
print(f"Number of characters is: {char_count}")
print(f"The longest word is: {longest}")
print(f"The shortest word is: {shortest}")
print(f"The number of words starting with a vowel: {vowel_start}")
print(f"The number of words ending with a vowel: {vowel_start}")
print(f"The number of words containing a digit: {digit}")