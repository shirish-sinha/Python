N = int(input("Enter a number: "))
product = 1
for i in range(N, 1, -1):
    if N == 0:
        break
    product *= i
print(product)