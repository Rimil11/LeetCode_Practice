# stones = [2,7,4,1,8,1]

# def lastStone(stones):
#     stones = sorted(stones)
#     print(stones)
#     while(len(stones)>=1):
#         if(len(stones)==1):
#             return stones[0]
#         print(f"Selected stones are: {stones[-1]} and {stones[-2]}")
#         new = abs(stones[-1] - stones[-2])
#         stones.pop()
#         if new!=0:
#             stones[-1]=new
#         else:
#             stones.pop()
#         stones = sorted(stones)
#         print(stones)
#     return new

# print(lastStone(stones))


# Using Heap
import heapq as hq

stones = [2,7,4,1,8,1]

def lastStone(stones):
    stones = [-s for s in stones]
    hq.heapify(stones)
    while(len(stones)>1):
        first = hq.heappop(stones)
        second = hq.heappop(stones)
        diff = first - second
        if diff!=0:
            hq.heappush(stones, diff)
    stones.append(0)
    return -stones[0]

print(lastStone(stones))