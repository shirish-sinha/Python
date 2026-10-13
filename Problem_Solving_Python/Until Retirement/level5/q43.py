str = input("Enter a string: ").lower()
chr = input("Enter the character: ")[0].lower()

if chr in str:
    print("true")
else:
    print("false")