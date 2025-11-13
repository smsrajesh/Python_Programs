
val = [10, 20, 30, [40, 50, [60, 70, [80, [90]]]]]

def Single_list(n, result=None):
    if result is None:
        result = []   # create new empty list first time

    for i in n:
        if isinstance(i, list):        # ✅ check if element is a list
            Single_list(i, result)     # recursive call if nested list
        else:
            result.append(i)           # add number to final list

    return result

result = Single_list(val)
print(result)


# def Single_list_1(n):
#     output=[]
#     for i in n:
#         print(f"{i} and its type is {type(i)}")
#         if type(i) is list:
#             output.extend(Single_list_1(i))
#         if type(i) is int:
#             output.append(i)
#         else:
#             pass
#     return output

# result = Single_list_1(val)
# print(result)

    


