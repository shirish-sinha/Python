bal = 5000
withdrawal = float(input("Enter amount to withdraw: "))

while withdrawal <= 0 or withdrawal > bal:
    print("Invalid amount entered")
    withdrawal = float(input("Re-enter amount to withdraw: "))

bal -= withdrawal

print(f"Balance: {bal}")