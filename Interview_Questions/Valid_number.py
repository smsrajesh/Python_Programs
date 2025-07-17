
"""
-->  It will start with 4,5 or 6.
-->  It will be 16 digits long(the numeric part).
-->  Numbers must contain only digits.
-->  It may have digits in groups separated by '-'.
"""


val="4-42325-78-8632-6589"
# val=input("Enter a value : ")
def valid(n):
    count=0
    num=['1','2','3','4','5','6','7','8','9']
    if n[0] in ['6','5','4']:
        for i in n:
            if i in num:
                count+=1
            elif i=="-":
                continue
            else:
                break
        if count==16:
            print("valid")
        else:
            print("Not valid")
    else:
        print("Not valid")

valid(val)
