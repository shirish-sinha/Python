code = input("Enter the code: ").lower()
valid = True
if len(code) == 8:
    for i in range(3):
        if not code[i].isalpha():
            valid = False
            break
    for i in range(3, 8):
        if not code[i].isdigit():
            valid = False
            break
    if valid:
        print("Valid Product Code")
    else:
        print("Invalid Product Code")
else:
    print("Invalid Product Code")