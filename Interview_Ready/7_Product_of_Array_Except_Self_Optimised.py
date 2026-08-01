# Question : Product of Array Except Self
# Input : 
input_1 = [1, 2, 3, 4]

# Expected_Output : [24, 12, 8, 6]


def Product_of_Array_Except_Self(nums):

    result = [0] * len(nums)

    l_product = 1
    left = [1]*len(nums)
    for i in range(1,len(nums)):
        l_product=l_product*nums[i-1]
        left[i]=l_product


    r_product = 1
    right = [1]*len(nums)
    for i in range(len(nums)-2,-1,-1):
        r_product=r_product*nums[i+1]
        right[i]=r_product
        

    for i in range(len(result)):
        result[i]=left[i]*right[i]

    return result

print(Product_of_Array_Except_Self(input_1))