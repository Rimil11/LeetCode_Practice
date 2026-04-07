def Is_monotonic_Array(nums):
    increasing = True
    decreasing = True
    for i in range(0,len(nums)-1):
        if(nums[i]>nums[i+1]):
            increasing = False
        elif(nums[i]<nums[i+1]):
            decreasing = False
        if(not increasing and not decreasing):
            return False

    return True


nums = [1,0,4]

print(Is_monotonic_Array(nums))