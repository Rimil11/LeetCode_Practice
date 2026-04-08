def rotate(nums, k):
    n = len(nums)
    k = k%n
    print(nums)
    def reverse(start, end):
        while(start<end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0,n-1)
    reverse(0,k-1)
    reverse(k, n-1)



rotate([-1,-100,3,99], 2)