def out():
    value=1
    def inn():
        nonlocal value
        print(value)

    inn()
out()