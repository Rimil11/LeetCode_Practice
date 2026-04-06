def max_sub(nums):
    max_sum = nums[0]
    curr_sum = 0
    j = len(nums)
    print(nums)
    i = 0
    k = 0
    while(i<j):
        curr_sum += nums[i]
        if(curr_sum>max_sum):
            max_sum = curr_sum
        if(curr_sum < 0):
            curr_sum = 0
        i+=1
    return max_sum




nums = [-2, -1, -3, -4, -1, -2, -1, -5, -4]
result = max_sub(nums)
print(result)
