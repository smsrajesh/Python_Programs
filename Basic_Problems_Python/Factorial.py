def fact(n):
    if n==0 or n==1:
        return 1
    else:
        result=n
        while n>2:
            n=n-1
            result=result*n
            print(f"RESULT IS = {result}")

    return f"result is {result}"

print(fact(n=int(input())))
