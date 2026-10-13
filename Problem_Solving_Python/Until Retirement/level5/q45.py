str = input("Enter a string: ").lower()
count = 0
for char in str:
    if char.isdigit():
        count += 1
print(count)