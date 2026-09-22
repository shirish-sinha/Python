a = int(input("Enter a number: "))

b = int(input("Enter another number: "))

c = int(input("Enter a third number: "))

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
elif b > a:
    if b > c:
        print(b)
    elif c > b:
        print(c)
else:
    print("All are equal")