# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"



# Approach 1: Nested loops
# def lcp_nested(strs):
#     if not strs:
#         return ""
#     result = ""
#     first = strs[0]
#     for i in range(len(first)):
#         for s in strs:
#             if i >= len(s) or s[i] != first[i]:
#                 return result
#         result += first[i]
#     return result


# Cleaned Version of the above code.

def cleaned_version(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix=prefix[:-1]
            if not prefix:
                return ""
    return prefix

print(cleaned_version(["flower","flow","flight"]))