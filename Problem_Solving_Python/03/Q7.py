string = input("Enter a string")
tested = ""
for char in string:
    if char not in tested:
        tested += char
        for i in range(len(string)):
            