str = input("Enter a string: ")
count = 0

for char in str:
    if "A" <= char <= "Z":
        count += 1
print(count)