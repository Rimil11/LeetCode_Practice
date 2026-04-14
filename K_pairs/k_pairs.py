import heapq as hq

def k_pairs_smallest(num1, num2, k):
    result = []
    if not num1 or not num2 or not k:
        return result
    heap = []
    visited = set()

    hq.heappush(heap, (num1[0]+num2[0], 0, 0))
    visited.add((0,0))

    while k and heap:
        
    
    return result

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(k_pairs_smallest(nums1,nums2, k))