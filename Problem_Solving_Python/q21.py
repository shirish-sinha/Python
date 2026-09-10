a = int(input("Enter length of side 1: "))
b = int(input("Enter length of side 2: "))
c = int(input("Enter length of side 3: "))

if a > 0 and b > 0 and c > 0:
    if (a + b) > c and (a + c) > b and (b + c) > a:
        if a == b == c:
            print("It is an equilateral triangle")
        elif a == b or a == c or b == c:
            print("It is and isosceles triangle")
        else:
            print("It is a scalene triangle")
    else:
        print("It is an invalid triangle")
    
else:
    print("Side cannot be negative")

    