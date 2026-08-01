# Problem: Top K Frequent Elements

# Input :

nums = [1,1,1,2,2,3]
k = 2

# Expected Output : [1,2]


def Top_K_Frequent_Elements(nums,k):
    
    freq={}
    result=[]
    for num in nums:
        freq[num]=freq.get(num,0)+1
    
    sorted_list=sorted(freq.items(), key=lambda x:x[1], reverse=True)
    
    print(sorted_list)
    
    for num, count in sorted_list:
        if k == 0:
            break
        result.append(num)
        k -= 1

    return result
    
print(Top_K_Frequent_Elements(nums,k))
    