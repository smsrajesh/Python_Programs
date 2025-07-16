print("-----Pizza Order Delivary-----")
order=input("What is the Order : ")
bill=0
if order.lower()=='pizza':
    order_size=input("Size is the Order : ")
    if order_size.lower()=='small':
        bill=100
        Extra=input(f"Pepperoni for {order_size} pizza (y/n): ")
        if Extra.lower()=='y':
            bill+=30
    elif order_size.lower()=='medium':
        bill=200
        Extra=input(f"Pepperoni for {order_size} pizza (y/n): ")
        if Extra.lower()=='y':
            bill+=50
    elif order_size.lower()=='large':
        bill=300
        Extra=input(f"Pepperoni for {order_size} pizza (y/n): ")
        if Extra.lower()=='y':
            bill+=50
    else:
        print(f"{order_size} is invalid")

    Extra_item=input("Extra Cheese (y/n):")
    if Extra_item.lower()=='y':
        bill+=20
    print(f"The total bill is {bill}")
else:
    print(f"{order} if not available...")