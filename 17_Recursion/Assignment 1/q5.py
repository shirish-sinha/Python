def counter_fun(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    return(counter_fun(n-1))

counter_fun(5)