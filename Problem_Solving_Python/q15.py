cp = int(input("Enter the cost price: "))
sp = int(input("Enter the selling price: "))

if sp > cp:
    print("Profit = ", sp - cp)
    print("Profit% = ", (sp - cp)/cp * 100)
elif cp > sp:
    print("Loss = ", cp - sp)
    print("Loss% = ", (cp - sp)/cp * 100)
else:
    print("No profit no loss")