str = input("Enter the string: ").lower()
count = 0

for char in str:
    if char not in "aeiou" and char != " ":
        count += 1
print(count)