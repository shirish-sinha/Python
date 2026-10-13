for i in range(5):
    upper = False
    lower = False
    digit = False
    special = False
    strength = 0

    password = input("Enter your password: ")

    if len(password) < 8:
        print("The minimum length of the password should be 8 characters")
    else:
        for char in password:
            if "A" <= char <= "Z":
                upper = True
            if "a" <= char <= "z":
                lower = True
            if "0" <= char <= "9":
                digit = True
            if ("!" <= char <= "/" or ":" <= char <= "@" or
                "[" <= char <= "`" or "{" <= char <= "~"):
                special = True

        strength = upper + lower + digit + special

        if strength <= 1:
            print("The password is weak")
        elif strength < 4:
            print("The password is medium")
        else:
            print("The password is strong")