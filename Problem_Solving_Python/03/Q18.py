bal = 5000
for i in range(7):
    act = input("Enter your action (deposit/withdraw): ").lower().strip()

    if act == "deposit":
        amt = int(input("Enter amount to deposit: "))
        bal += amt
        print(f"Balance: {bal}")
    elif act == "withdraw":
        amt = int(input("Enter amount to withdraw: "))
        if amt > bal:
            print("Withdrawal amount cannot be greater than the balance.")
            break
        else:
            bal -= amt
            print(f"Balance: {bal}")
    else:
        print("You did not choose a valid operation")
        break
    if bal < 1000:
        print("Low Balance")