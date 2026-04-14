def k_smallest(nums1, nums2, k):
    smallest = []
    first = [nums1[0],nums2[0]]
    second = [nums1[0],nums2[0]]
    third = [nums1[0],nums2[0]]
    for i in range(nums1.length):
        for j in range(nums2.length):
            currSum = nums1[i] + nums2[j]
            if currSum < first.sum():
                third = second
                second = first
                first = [nums1[i], nums2[j]]
    
    return smallest