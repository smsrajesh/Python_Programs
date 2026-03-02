def valid_paranthesis(s):
    result=[]
    mapp={")":"(","]":"[","}":"{"}
    for ch in s:
        if ch not in mapp:
            result.append(ch)
        else:
            if result and result[-1]==mapp[ch]:
                result.pop()
            else:
                return False
            
    return True if not result else False

print(valid_paranthesis(input("Enter the string: ")))



# if not result: 
#     return True
# else:
#     return False

# If result is empty ([]) → not result becomes True → returns True

# If result is not empty ([1,2]) → not result becomes False → returns False