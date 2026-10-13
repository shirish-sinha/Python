odd = 0
even = 0
for i in range(5):
    number = int(input("Enter a number: "))
    number = str(number)

    for num in number:
        num = int(num)
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

if even > odd:
    print("Even")
elif odd > even:
    print("Odd")
else:
    print("Tie")