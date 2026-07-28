'''
    Problem 5 — Return Longest Substring
        Problem Statement :
            Instead of returning the length, Return the substring itself.

    Example :

        Input : abcdbcdda
        Output : abcd


    Test Cases :

            abcdbcdda

            abcdef

            aaaa

            abba

            pwwkew

'''


input_1 = 'abcdbcdda'

def Longest_Substring_String(s):

    result=set()

    left = 0
    longest = 0

    start = 0

    for right in range(len(s)):

        while s[right] in result:
            result.remove(s[left])
            left+=1

        result.add(s[right])

        tentative_longest = right - left + 1

        if tentative_longest>longest:
            longest=tentative_longest
            start=left

    print(start,longest)

    return [longest,s[start:start+longest]]

print(Longest_Substring_String(input_1))