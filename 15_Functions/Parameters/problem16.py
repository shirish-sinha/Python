def format_name(first, last, uppercase=False):
    full_name = f"{first} {last}"
    if uppercase:
        return full_name.upper()
    return full_name


print(format_name("Asha", "Patel"))
print(format_name("Asha", "Patel", True))
