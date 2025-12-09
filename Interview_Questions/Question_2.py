
'''
    input=abbcccdddd
    output=abcd
'''

'''
    text = "hello   world"
    print(text.replace(" ", ""))
'''

def fun(a):
    result=""
    for i in a:
        if i not in  result:
            result+=i
    return result.replace(" ","")

print(fun(input("Enter a string with duplicate letters :")))