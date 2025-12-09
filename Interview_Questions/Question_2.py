

'''
    input=abbcccdddd
    output=abcd
'''


def fun(a):
    result=""
    for i in a:
        if i not in  result:
            result+=i
    return result

print(fun(input("Enter a string with duplicate letters without any gaps :")))