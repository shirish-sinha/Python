x = 1
def outer ():
    x = 2

    def inner ():
        x = 3
        print(x)
    inner()
    print(x)

outer()
print(x)
