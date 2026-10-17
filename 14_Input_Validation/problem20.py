# count = int(input("Enter the count of numbers you wish to enter: "))

# while count < 1 or count > 20:
#     print("Out of the given range(1-20)")
#     count = int(input("Re-enter the count of numbers you wish to enter: "))

# total = 0

# for i in range(count):
#     num = int(input("Enter the number: "))
#     total += num
#     print(f"Total: {total}")

# average = total/count

# print(f"Average: {average}")

while True:
    n = int(input("Enter a number between 1 and 20: "))
    if 1<=n<=20:
        break
    else:
        print("Invalid input, try again: ")
total=0
for i in range(1,n+1):
    while True:
        number=float(input(f"Enter number {i}: "))
        total += number
        break
average=total/n
print("Average: ", average)