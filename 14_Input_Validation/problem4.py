print("""Menu:
    1. View profile
    2. Edit profile
    3. Settings
    4. Exit""")

choice = int(input("Enter your choice: "))

while not 1 <= choice <= 4:
    choice = int(input("Enter a correct choice: "))

match(choice):
    case 1:
        print("View Profile")
    case 2:
        print("Edit profile")
    case 3:
        print("Settings")
    case 4:
        print("Exit")