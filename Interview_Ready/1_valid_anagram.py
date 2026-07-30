'''

    Problem 1 — Valid Anagram
    1. Problem Statement :

    Given two strings s and t, determine whether t is an anagram of s.

    Two strings are anagrams if they contain the same characters with the same frequencies.


    Example :

        Input:
        s="eat"
        t="tea"

        Output:
        True


    Test Cases :

        ("eat","tea")      -> True
        ("rat","car")      -> False
        ("listen","silent")-> True
        ("hello","world")  -> False
        ("","")            -> True

'''


"""

    2. Brute Force

        Sort both strings and compare.

        Code :-

        def isAnagram(s,t):

            return sorted(s)==sorted(t)

"""


input1 ="eat"
input2 ="tea"

def valid_anagram(s,t):

    if len(s)!=len(t):
        return False

    count=[0]*26

    for i in s:
        index=ord(i)-ord('a')
        count[index]+=1
    for i in t:
        count[ord(i)-ord('a')]-=1

    return all(i==0 for i in count)


print(valid_anagram(input1,input2))







# i1 = ""
# i2 = ""
# def valid_anagram_2(s,t):

#     if len(s)!=len(t):
#         return False

#     return sorted(s)==sorted(t)

# print(valid_anagram_2(i1,i2))



def valid_anagram_2(s, t):

    if len(s) != len(t):
        return False

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq:
            return False

        freq[ch] -= 1

        if freq[ch] == 0:
            del freq[ch]

    return len(freq) == 0


print(valid_anagram_2("1smsr", "rsms1"))