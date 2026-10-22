def calculate_pay(hours, rate=200, bonus=0):
    return hours * rate + bonus


print(calculate_pay(8))
print(calculate_pay(8, 250))
print(calculate_pay(8, bonus=100))
print(calculate_pay(8, rate=250, bonus=100))
