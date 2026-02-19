import heapq as hq

def k_pairs_smallest(num1, num2, k):
    hq.heapify(num1)
    hq.heapify(num2)
    count = 0
    result = []
    while(count<3):
        result.append([hq.heappop(num1), hq.heappop(num2)])
        count+=1
    return result

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(k_pairs_smallest(nums1,nums2, k))