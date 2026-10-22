def bill(item, quantity=1, price=100):
    return quantity * price


print(bill("Book"))
print(bill("Pen", 3, 10))
print(bill("Notebook", price=50, quantity=2))
