
num_list=list()
num=int(input("Enter how many values you want in a list : "))
for i in range(num):
    num_list.append(int(input(f"Enter {i} th element : ")))
def second_maximum(n):
    max=s_max=0
    for i in n:
        if max<i:
            s_max=max
            max=i
        elif s_max<i and max>i:
            s_max=i
    # print(f"first maximum is {max}")
    print(f"second maximum is {s_max}")

second_maximum(num_list)
