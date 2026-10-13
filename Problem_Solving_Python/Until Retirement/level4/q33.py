str = input("Enter the string: ").lower()
count = 0

for char in str:
    if char in "aeiou":
        count += 1
print(count)