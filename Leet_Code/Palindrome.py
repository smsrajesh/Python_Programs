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