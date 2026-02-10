

# def count(F_str,S_str,result=0):
#     for i in range(len(F_str)-len(S_str)+1):
#         if F_str[i:i+len(S_str)]==S_str:
#             result+=1
#     return f"{S_str} in {F_str} for {result} times."


# print(count("abcdefg","def"))
# print(count('hello','world'))
# print(count('mississippi','iss'))
# print(count('she sells seashells by the seashore','sh'))
# print(count('101010101010101010101','101'))



# Q1. INPUT:
# l1=['a','b','c'],l2=['d','e','f']
    # OUTPUT:
    # ['a','b','c','d','e','f']


# l1=list(map(str,input("Enter values").split(",")))
# l2=list(map(str,input("Enter values").split(",")))

# n=0
# empty_list=[]

# if len(l1)>len(l2):
#     n=len(l1)
#     for i in range(n):
#         empty_list.append(l1[i])
#         if len(l2)>i:
#             empty_list.append(l2[i])
#         else:
#             continue

# else:
#     n=len(l2)
#     for i in range(n):
#         if len(l1)>i:
#             empty_list.append(l1[i])
#         else:
#             pass
#         empty_list.append(l2[i])


# print(empty_list)

    

# Q2.First non repeating char from string in python

def nrc(s):
    d={}
    for i in s:
        # print(i)
        d[i]=d.get(i,0)+1
    # print(d)
    for i in d.keys():
        # print(i," ",d[i])
        if d[i]==1:
            return i
    return "No non repeating char found."

print(nrc("aabc"))


# Q3.Flatten the list in python

l1=[[1,2],[3,[4]],[5,6]]
def flatten(n,res=None):
    if res is None:
        res=[]
    for i in n:
        if type(i)==list:
            flatten(i,res)
        else:
            res.append(i) 
    return res

print(flatten(l1))


# l1=[[1,2],[3,[4]],[5,6]]
# def flatten_1(n):
#     res=[]
#     for i in n:
#         if type(i)==list:
#             res.extend(flatten_1(i))
#         else:
#             res.append(i)
#     return res

# print(flatten_1(l1))