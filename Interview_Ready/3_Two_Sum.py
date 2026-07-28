'''
    Problem 3 — Two Sum

        Problem Statement : Return indices of two numbers whose sum equals target.

    Example :

            nums=[2,7,11,15]

            target=9

            Output : [0,1]


    Test Cases : 
            [3,2,4],6

            [3,3],6

            [1,5,7,8],13

            [10,20],30

            
'''


input_1, input_2  = [10,20],30

def two_sum(nums,target):

    groups={}
    for i,num in enumerate(nums):

        result=target-num
        if result in groups:
            print(groups[result],i)

        groups[num] = i


two_sum(input_1,input_2)

