def convert_temperature(value, scale="C"):
    if scale == "C":
        return value * 9 / 5 + 32
    return (value - 32) * 5 / 9


print(convert_temperature(25))
print(convert_temperature(77, "F"))
