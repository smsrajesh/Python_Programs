'''
    Problem 2 — Group Anagrams

        Problem Statement : Group words that are anagrams.

    Example :

        Input : ["eat","tea","tan","ate","nat","bat"]

        Output :
                [
                    ["eat","tea","ate"],
                    ["tan","nat"],
                    ["bat"]
                ]


    Test Cases :

        [""]

        ["a"]

        ["abc","cab","bac","xyz"]

        ["cat","dog","god","tac"]

'''


"""
    Brute Force : 
        Compare every string with every other string.

"""


# input1 = ["eat","tea","tan","ate","nat","bat"]

# def group_anagram_v1(words):

#     groups={}

#     for word in words:
#         key="".join(sorted(word))

#         if key not in groups:
#             groups[key]=[]

#         groups[key].append(word)


#     return list(groups.values())

# print(group_anagram_v1(input1))




input2 = ["abc","cab","bac","xyz"]

def group_anagram_v2(words):

    groups = {}

    for word in words:
        count=[0]*26
        for ch in word:
            index=ord(ch)-ord('a')
            count[index]+=1

        key = tuple(count)

        if key not in groups:
            groups[key]=[]

        groups[key].append(word)


    return list(groups.values())

print(group_anagram_v2(input2))



