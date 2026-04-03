

def func(nums):
    x1, y1 = nums.pop()
    time = 0
    while(nums):
        x2, y2 = nums.pop()
        time += max(abs(x2-x1), abs(y2-y1))
        x1, y1 = x2, y2
    return time

print(func([[1,1],[3,4],[-1,0]]))