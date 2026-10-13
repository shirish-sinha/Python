for i in range(1, 11):
    if i == 6:
        break
    print(i)

numbers = [10, 20, 30, 40, 50]
for i in numbers:
    if i == 30:
        print("Found")
        break

while True:
    n = int(input("Enter a number: "))
    if n == 0:
        break

for i in range(1, 101):
    if i % 17 == 0:
        break
    print(i)
