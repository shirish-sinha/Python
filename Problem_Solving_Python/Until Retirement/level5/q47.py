str = input("Enter a string: ")
count = 0

for char in str:
    if "a" <= char <= "z":
        count += 1
print(count)