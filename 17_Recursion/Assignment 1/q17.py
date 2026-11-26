# def stop_at_zero(n):
#     if n == 0:
#         return

#     stop_at_zero(n)

def stop_at_zero(n):
    if n == 0:
        return

    stop_at_zero(n-1)