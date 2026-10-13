# row = int(input("Enter the number of rows: "))

# for i in range(1, row + 1):
#     for j in range(1, i+1):
#         prime = True
#         for k in range(2,j):
#             if j % k == 0:
#                 prime = False
#         if prime and j != 1:
#             print("P", end=" ")
#         elif j % 2 == 0:
#             print("E", end=" ")
#         else:
#             print("O", end=" ")    
#     print()

limit = int(input("Enter the range: "))

for i in range(2, limit):
    prime = True
    for j in range(2,i):
        if  i % j == 0:
            prime = False
        else:
            continue
    if prime:
        print(i)