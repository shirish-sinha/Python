count = 0
def counter_fun(n):
    global count
    if count == n:
        return
    count += 1
    print(count)
    
    return(counter_fun(n))

counter_fun(5)

# def counter(n):
#     if n == 0:
#         return
#     counter(n-1)
#     print(n)

# counter(4)