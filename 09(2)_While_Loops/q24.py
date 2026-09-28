text = input("Enter a string: ")
index = 0
a_count = 0
while index < len(text):
    if text[index] == "a":
        a_count += 1
    index += 1
print('Number of "a" characters:', a_count)