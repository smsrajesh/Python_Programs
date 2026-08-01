# Question : Product of Array Except Self
# Input : 
input_1 = [1, 2, 3, 4]

# Expected_Output : [24, 12, 8, 6]


def Product_of_Array_Except_Self(nums):
    result = [0] * len(nums)

    for i in range(len(nums)):

        val = 1
        for j in range(len(nums)):
            if i == j:
                continue
            else:
                val = val * nums[j]

        result[i] = val

    return result

print(Product_of_Array_Except_Self(input_1))