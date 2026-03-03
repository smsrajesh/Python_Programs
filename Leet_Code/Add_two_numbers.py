# def two_sum(nums,target):
#     result=[]
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 result.append(i)
#                 result.append(j)
#                 break
#         if len(result)!=0:
#             break
#     return result

# print(two_sum([1,2,5,3,4,7],target=8))



def twoSum(nums: list[int], target: int) -> list[int]:
    dic={}
    for i, v in enumerate(nums):
        k=target-v
        if k in dic:
            return [dic[k], i]
        dic[v] = i

nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target: "))

print(twoSum(nums,target))


# def twoSum(nums: list[int], target: int) -> list[int]

# "These are Python type hints. They specify expected input and output types, 
#  but Python does not strictly enforce them at runtime."

# def twoSum(nums, target):

# It will work exactly the same.

# Type hints are just for clarity and professional coding style.
        