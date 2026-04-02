
def missingNumber(nums):

    # 1st Approach
    # nums.sort()
    # i = 0
    # while(i<len(nums)):
    #     if (i!=nums[i]):
    #         return i
    #     i+=1
    # return i

    # 2nd Approach
    n = len(nums)
    sumOfN = n*(n+1)//2
    return sumOfN - sum(nums)
    
print(missingNumber([0,2,3]))
