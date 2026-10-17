username = input("Enter the username: ").strip()

while len(username) <= 5 or " " in username:
    print("Invalid username")
    username = input("Enter a valid username: ").strip()

password = input("Enter the username: ").strip()

while len(password) <= 8 or password == "":
    print("Invalid password")
    password = input("Enter a valid password: ").strip()

print("Success")