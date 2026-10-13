sequence = ""
current = 1
previous = 0
lim = int(input("Enter the limit: "))

for i in range(lim):
    sequence += str(previous) + " "
    previous, current = current, current + previous

print(sequence)