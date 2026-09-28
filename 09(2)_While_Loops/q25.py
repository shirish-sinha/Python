text = input("Enter a string: ")
index = 0
uppercase_count = 0
while index < len(text):
    if text[index].isupper():
        uppercase_count += 1
    index += 1
print("Number of uppercase letters:", uppercase_count)