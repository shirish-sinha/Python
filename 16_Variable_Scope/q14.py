def outer ():
    name = "Sumit"

    def inner ():
        print(name)

    return inner 

result = outer()
result()