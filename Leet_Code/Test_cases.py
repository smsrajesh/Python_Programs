
# Largest_String_Prefix  and  Valid_Paranthesis

# result=input("Enter a name : ")
# i=0
# while i<5:
#     print(result,end=" ")
#     print(result[-1])
#     result=result[:-1]
#     i+=1


# Valid_Paranthesis

def che(result):
    if result:
        return True
    else:
        return False

result=list(map(int,input("Enter int values : ").split()))
print(che(result))

# If u pass an empty_list, then the function returns False.
# If u pass an list with elements, then the function returns True.

