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



# Optimised way to check if a number is a palindrome without converting it to a string.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x % 10 == 0 and x != 0:
            return False
        
        reversed_half = 0
        
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        return x == reversed_half or x == reversed_half // 10


# Solution - 1 : it stores as list.

s=input("Enter a string: ")

k=[i.lower() for i in s if i.isalnum()]

if k==k[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")


#  Solution - 2 : it stores as String.

s=input("Enter a string: ")

k="".join(i.lower() for i in s if i.isalnum())

if k==k[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")



# Optimized way to find the given strig is palindrome or not.

s = input("Enter a string: ")

i = 0
j = len(s) - 1

while i < j:

    if not s[i].isalnum():
        i += 1
        continue

    if not s[j].isalnum():
        j -= 1
        continue

    if s[i].lower() != s[j].lower():
        print("Not a Palindrome")
        break

    i += 1
    j -= 1

else:
    print("Palindrome")