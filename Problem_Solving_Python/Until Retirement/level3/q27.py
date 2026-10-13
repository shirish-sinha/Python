lim = int(input("Enter a number: "))

for i in range(2, lim):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i)