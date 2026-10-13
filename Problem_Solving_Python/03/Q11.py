dig_count = 0
uscore_count = 0
valid = True
for i in range(5):
    if valid:
        name = input("Enter the username: ")
        print(len(name))
        print(name[0])
        for char in name:
            if "0" <= char <= "9":
                dig_count += 1
            elif char == "_":
                uscore_count += 1
            elif ("!" <= char <= "/" or ":" <= char <= "@" or "[" <= char <= "`" or "{" <= char <= "~"):
                valid = False
        if dig_count >= 1 and uscore_count >= 1:
            print("Valid")
        else:
            print("Needs Improvement")
        print(f"Digits: {dig_count}")
        print(f"Underscores: {uscore_count}")
    else:
        print("Enter a valid password without special characters")
        break