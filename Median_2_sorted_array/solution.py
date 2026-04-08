def solution(nums1, nums2):
    i = 0
    j = 0
    m = len(nums1)
    n = len(nums2)
    nums3 = []
    while(i<m and j<n):
        if(nums1[i]<nums2[j]):
            nums3.append(nums1[i])
            i += 1
        else:
            nums3.append(nums2[j])
            j += 1
        print("Nums3: ", nums3) 
        
    while(i<m):
        # nums3.extend(nums2[j:n])
        nums3.append(nums1[i])
        i+=1
    while(j<n):
        # nums3.extend(nums1[i:m])
        nums3.append(nums2[j])
        j+=1

    size = len(nums3)
    if size%2==0:
        median1 = size//2
        median2 = median1 - 1
        return (nums3[median1] + nums3[median2])/2.0
    else:
        median1 = size//2
        return nums3[median1]

nums1 = [1,2]
nums2 = [3,4]

print("Medians: ",solution(nums1, nums2))