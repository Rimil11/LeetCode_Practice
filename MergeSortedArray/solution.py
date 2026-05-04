def merge(nums1, m, nums2, n):
    i = m-1
    j = n-1
    k = m+n -1
    print(nums1)
    temp = None
    while(j>=0 and i>=0):
        if(nums2[j] > nums1[i]):
            nums1[k] = nums2[j]
            k-=1
            j-=1
        else:
            temp = nums1[i]
            nums1[i] = nums2[j]
            nums1[k] = temp
            i-=1
            k-=1
        print("Nums1: ", nums1)

    while(j>=0):
        nums1[k] = nums2[j]
        k-=1
        j-=1
    print("Nums1: ", nums1)


nums1 = [0,0,0]
nums2 = [1,1,6]
m,n = 0,3
merge(nums1, m, nums2, n)