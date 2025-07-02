name=input("Enter the Value : ")
result=""
for i in range(len(name)-1,-1,-1):
    print(name[i])
    result+=name[i]

"""
Reverse of a String using in-built functions

result=name[::-1]
print(result)

"""


if(name==result):
    print(f"{name} is a palindrome")
else:
    print(f"{name} is not a palindrome")


