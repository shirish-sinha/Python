str = input("Enter the string: ").strip().lower()

for char in str:
    if char == "o":
        print("Found")
        break
else:
    print("Not found")