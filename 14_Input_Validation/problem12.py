balance = 2000

deposit = int(input("Enter amount to deposit: "))

while deposit < 0:
    print("Deposit cannot be negative")
    deposit = int(input("Enter amount to deposit: "))

print(f"Balance: {balance + deposit}")