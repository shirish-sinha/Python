# Problem 30

print("placed")
print("confirmed")
print("preparing")
print("out_for_delivery")
print("delivered")
print("cancelled")

status = input("Enter status: ").strip().lower()

match status:
    case "placed":
        print("Your order has been placed")
    case "confirmed":
        print("Your order has been confirmed")
    case "preparing":
        print("Your order is being prepared")
    case "out_for_delivery":
        print("Your order is on the way")
    case "delivered":
        print("Your order has been delivered")
    case "cancelled":
        print("Your order has been cancelled")
    case _:
        print("Invalid Order Status")