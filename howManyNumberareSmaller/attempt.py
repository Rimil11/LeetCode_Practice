
def func(nums):
    temp = sorted(nums)
    dict = {}
    for i, n in enumerate(temp):
        if n not in dict:
            dict[n] = i
    result = []
    for element in nums:
        result.append(dict[element])
    
    return result



nums = [2,3,2,1,7,1]
print(func(nums))