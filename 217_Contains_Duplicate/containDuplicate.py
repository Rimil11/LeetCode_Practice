def containsDuplicate(nums):

    # 1st Approach
    # seen = set()
    # for element in nums:
    #     if element in seen:
    #         return True
    #     else:
    #         seen.add(element)
    # return False

    # 2nd Approach
    setnums = set(nums)
    if(len(setnums)!=len(nums)):
        return True
    else:
        return False
    
print(containsDuplicate([1,2,3,2]))
print(containsDuplicate([1,2,3]))