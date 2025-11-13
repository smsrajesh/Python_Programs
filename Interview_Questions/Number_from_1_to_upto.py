






def Sequence(number,result=""):
    if number<=0:
        return "Invalid Input"
    else:
        for i in range(1,number+1):
            result+=str(i)
        return result


print(Sequence(5))
print(Sequence(10))
print(Sequence(1))
print(Sequence(27))
print(Sequence(-5))