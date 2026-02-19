# def func(heights):
#     larg = -1
#     for i,height in enumerate(heights):
#         print("Current Details:-")
#         print("Index: ", i)
#         print("Height: ", height)

#         l = i
#         while(l>0 and heights[l-1]>=height):
#             l-=1
#         print("Left: ", l)

#         r = i
#         while(r<len(heights)-1 and heights[r+1]>=height):
#             r+=1
#         print("Right: ", r)

#         currentArea = (r-l+1)*height

#         print("Current Area: ", currentArea)
#         if(larg<currentArea):
#             larg = currentArea
#         print("---------------------")
#     return larg

# print("Largest rectangle area: ",func([2,4]))


# Efficient Approach

def func(heights):
    stack = []
    larg = -1
    for i, height in enumerate(heights):
        print("Index: ", i)
        last = i
        while(stack and stack[-1][1]>height):
            currentArea = (i - stack[-1][0])*stack[-1][1]
            # i = stack[-1][0]
            print("Current Area: ", currentArea)
            popped = stack.pop()
            last = popped[0]
            if (currentArea > larg):
                larg = currentArea
        stack.append([last, height])
                
        print("Stack: ",stack)

    while(stack):
        currentArea = (len(heights) - stack[-1][0]) * stack[-1][1]
        if currentArea>larg:
            larg = currentArea
        stack.pop()
    print("Final Stack: ", stack)
    return larg

print("Largest rectangle area: ",func([2,1,5,6,2,3]))
