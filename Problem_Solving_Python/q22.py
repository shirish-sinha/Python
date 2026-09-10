balance = int(input("Enter your balance: "))
withdrawal_amt = int(input("Enter withdrawal amount: "))

if withdrawal_amt > 0 and withdrawal_amt % 100 == 0 and withdrawal_amt < (balance - 500):
    balance = balance - withdrawal_amt
    print("Withdrawal Successful")
    print(f"Remaining balance: {balance}")
else:
    print("Please enter a valid amount")