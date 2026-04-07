
def pivotIndex(nums):

    # Brute Force
    # l = len(nums)
    # for i in range(l):
    #     if(sum(nums[0:i]) == sum(nums[i+1:l])):
    #         return i
    # return -1


    # Efficient
    total = sum(nums)
    l = len(nums)
    l_sum = 0
    for i in range(l):
        r_sum = total - nums[i] - l_sum
        if(r_sum == l_sum):
            return i
        l_sum += nums[i]
    return -1
    


nums = [2,1,-1, 3]
print(pivotIndex(nums))