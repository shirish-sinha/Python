def classify_number(number):
    if number > 0:
        return "Positive"
    if number < 0:
        return "Negative"
    return "Zero"


print(classify_number(5))
print(classify_number(-2))
print(classify_number(0))
