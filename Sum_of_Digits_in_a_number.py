# var_a=int(input("Enter value of a = "))
# temp=var_a
# sum_of_digits=0
# while temp>0:
#     remainder=int(temp%10)
#     sum_of_digits+=remainder
#     temp=temp//10

# print(sum_of_digits)


var_s=input("Enter value of s = ")
sum_of_digits=0
for i in var_s:
    sum_of_digits+=int(i)

print(sum_of_digits)

