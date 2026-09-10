name1, age1 = input("Enter your name and age: ").split()
name2, age2 = input("Enter your name and age: ").split()
name3, age3 = input("Enter your name and age: ").split()

if age1 < age2:
    if age1 < age3:
        print(name1)
    else:
        print(name3)
elif age2 < age3:
    if age2 < age1:
        print(name2)
    else:
        print(name1)
else:
    print(name3)