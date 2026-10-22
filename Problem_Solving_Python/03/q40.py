string1 = input("Enter the string: ").strip()
string2 = input("Enter the mirror string to check: ").strip()

if len(string1) == len(string2):
    for i in range(len(string1)):
        if string1[i] == string2[len(string2) - i - 1]:
            continue
        else:
            print("Not a mirror string")
            break
    else:
        print("It is a mirror string")
else:
    print("Not a mirror string")