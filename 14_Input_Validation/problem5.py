password = input("Enter a password: ").strip()

while len(password) < 8:
    print("Password must be atleast 8 characters")
    password = input("Enter a password: ").strip()
else:
    print("Success")