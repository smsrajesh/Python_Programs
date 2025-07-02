""" WAP to Calculate Average height from a list of heights
    without using In-built functions (WUIF)"""


# size=int(input("Enter the Size : "))
# height_list=[]
# sum=0
# for i in range(size):
#     height_list.append(int(input(f"Enter {i} elements in the List : ")))
#     sum+=height_list[i]
# print(sum/size)
# print(f"Average of height_list is {round(sum/size)}")



""" WAP to find Maximum number without using In-built Functions (WUIF)"""

# size=int(input("Enter the Size : "))
# num_list=[]
# max=0
# for i in range(size):
#     num_list.append(int(input(f"Enter {i} elements in the List : ")))
#     if max<num_list[i]:
#         max=num_list[i]

# print(f"Maximum number from the num_list is {max}")


""" WAP to find Sum of the numbers statinf from (1 to 100) """

# sum=0
# for i in range(1,101):
#     sum+=i

# print(f"Sum of 1 to 100 is {sum}")


""" WAPTF sum  of even numbers from (1 to 100) """

# # type : 1

# even_sum=0
# for i in range(2,101,2):
#     even_sum+=i
# print(f"Even_numbers Sum from 1 to 100 is {even_sum}")

# # type : 2
     
# even_sum=0
# for i in range(1,101):
#     if i%2==0:
#         even_sum+=i
# print(f"Even_numbers Sum from 1 to 100 is {even_sum}")


""" Problem Statement : 
    if num is divisible by 3 then print "Fizz"
    if num is divisible by 5 then print "Byzz"
    if num is divisible by both 3 and 5 then print "FizzByzz"
    else print the number as it is.
"""

num=int(input("Enter the Number : "))
for i in range(num+1):
    if i%3==0:
        if i%5==0:
            print("FizzByzz")
        else:
            print("Fizz")
    elif i%5==0:
        print("Byzz")
    else:
        print(i)





