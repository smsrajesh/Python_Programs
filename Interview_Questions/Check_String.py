








def count(F_str,S_str,result=0):
    for i in range(len(F_str)-len(S_str)+1):
        if F_str[i:i+len(S_str)]==S_str:
            result+=1
    return f"{S_str} in {F_str} for {result} times."


print(count("abcdefg","def"))
print(count('hello','world'))
print(count('mississippi','iss'))
print(count('she sells seashells by the seashore','sh'))
print(count('101010101010101010101','101'))



