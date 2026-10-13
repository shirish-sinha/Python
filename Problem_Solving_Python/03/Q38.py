stc = input("Enter a sentence: ").split()
checked = ""
for word in stc:
    count = 1
    if word not in checked:
        checked += word + " "
    else:
        count += 1
    print(f"{word}: {count}")
