def duplicate(nums, k):
    seen = {}
    i = 0
    while(i<len(nums)):
        print("INdex: ", i)
        if(nums[i] in seen.keys()):
            prevIndex = seen[nums[i]]
            diff = abs(i-prevIndex)
            seen[nums[i]] = i
            print("Current element: ", nums[i])
            print("Abs diff: ", diff)
            print()
            if(diff<=k):
                return True
        else:
            seen[nums[i]] = i
        i+=1
    return False

nums = [1,2,3,1,2,3]
k = 2

print("Final: ", duplicate(nums, k))