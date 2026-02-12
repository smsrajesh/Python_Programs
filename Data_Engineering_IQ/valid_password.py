# def val_pass(s):
#     if len(s)>=8 and any(c.isupper() for c in s) and any(c.isdigit() for c in s)\
#     and any(c in '!@#$%^&' for c in s): 
#         return True
#     return False
# n=input("Enter a password: ")
# if val_pass(n):
#     print(f"{n} is a Valid Password")
# else:
#     print(f"{n} is an Invalid Password")




def val_pass(s):
    if len(s)>=8 and any(c.isupper() for c in s) and any(c.isdigit() for c in s)\
    and any(not c.isalnum() for c in s): 
        return True
    return False
n=input("Enter a password: ")
if val_pass(n):
    print(f"{n} is a Valid Password")
else:
    print(f"{n} is an Invalid Password")