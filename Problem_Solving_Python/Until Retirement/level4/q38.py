string = input("Enter a string: ")

i = 0
j = len(string)-1

while i < j:
    if string[i] == string[j]:
        i += 1
        j -= 1
    else:
        print("Not a palindrome")
        break
else:
    print("It is a palindrome")