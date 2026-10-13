string = input("Enter a string: ").lower()
count = 0
for char in string:
    if char == "a":
        count += 1

print(count)