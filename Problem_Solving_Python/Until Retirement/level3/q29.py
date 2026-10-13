a = 10
b = 120

gcd = 0

if a > b:
    for i in range(1, int(b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
elif b > a:
    for i in range(1, int(a) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
else:
    gcd = a

print(f"GCD = {gcd}")