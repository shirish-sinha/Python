username = input("Enter your username: ")

while len(username) < 5 or " " in username or username == "":
    username = input("Enter a valid username: ")
else:
    print(username)