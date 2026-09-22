Username = "admin"
Password = "python123"

username = input("Enter the username: ")
password = input("Enter the password: ")

if username == Username and password == Password:
    print("Login Successful")
elif username == Username and password != Password:
    print("Wrong password")
else:
    print("User not found")