'''
    Problem 4 — Longest Substring Length
    
        Problem Statement : Return the length of the longest substring without repeating characters.

    Example :

        Input : abcabcbb
        Output : 3

    Test Cases : 

        abcabcbb

        bbbbb

        pwwkew

        abba

        abcdef

        aaaa

        dvdf

        tmmzuxt

'''


input_1 = 'abcdef'

def longest_substring(s):

    left=0
    longest=0

    result=set()

    for right in range(len(s)):

        while s[right] in result:
            result.remove(s[left])
            left+=1

        result.add(s[right])

        longest=max(longest,right-left+1)

    return longest

print(longest_substring(input_1))