sentence = input("Enter a string: ").lower()
same_pair = 0
diff_pair = 0
vowel_pair = 0
dig_pair = 0

for i in range(len(sentence)):
    for char in range(i + 1, len(sentence)):
        if sentence[i] == sentence[char]:
            same_pair += 1
            if (sentence[i] == "a" or sentence[i] == "e" or sentence[i] == "i" or sentence[i] == "o" or sentence[i] == "u") and (sentence[char] == "a" or sentence[char] == "e" or sentence[char] == "i" or sentence[char] == "o" or sentence[char] == "u"):
                vowel_pair += 1
            elif "0" <= sentence[i] <= "9" and "0" <= sentence[char] <= "9":
                dig_pair += 1
        else:
            diff_pair += 1
            if (sentence[i] == "a" or sentence[i] == "e" or sentence[i] == "i" or sentence[i] == "o" or sentence[i] == "u") and (sentence[char] == "a" or sentence[char] == "e" or sentence[char] == "i" or sentence[char] == "o" or sentence[char] == "u"):
                vowel_pair += 1
            elif "0" <= sentence[i] <= "9" and "0" <= sentence[char] <= "9":
                dig_pair += 1


print(f"There are {same_pair} pairs of same characters")
print(f"There are {diff_pair} pairs of different characters")
print(f"There are {vowel_pair} pairs of vowels")
print(f"There are {dig_pair} pairs of digits")