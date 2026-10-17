is_running = True
bal = 10000

print("""Available Choices:
                    1. Check balance
                    2. Deposit money
                    3. Withdraw money
                    4. Exit""")



while is_running:
    choice = int(input("Enter the operation (1-4): "))
    match(choice):
        case 1:
            print(f"Balance: {bal}")
        case 2:
            deposit = float(input("Enter amount to deposit: "))
            if deposit <= 0:
                print("You entered an invalid amount")
                continue
            else:
                bal += deposit
                print(f"Updated Balance: {bal}")
        case 3:
            withdrawn = float(input("Enter amount to withdraw: "))
            if withdrawn > bal or withdrawn <= 0:
                print("You entered an invalid amount")
                continue
            else:
                bal -= withdrawn
                print(f"Updated Balance: {bal}")
        case 4:
            print("Thank you for using our services.")
            is_running = False
        case _:
            print("You did not enter a valid choice.")
