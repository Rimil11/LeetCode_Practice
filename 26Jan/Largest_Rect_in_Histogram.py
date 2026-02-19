def func(heights):
    larg = -1
    for i,height in enumerate(heights):
        print("Index: ",i)
        l = i-1
        while(l>0 and heights[l-1]>height):
            # if(height>heights[l]):
            #     l+=1
            #     break
            l-=1

        r = i+1
        while(r<len(heights)-1):
            if(height>heights[r+1]):
                r-=1
                break
            r+=1
        currentArea = (r-l+1)*height
        if(currentArea>larg):
            larg = currentArea
        
        print("Left index: ",l)
        print("Right index: ", r)
        print("Current Area: ", currentArea)
    return larg

print("Largest rectangle area: ",func([2,1,5,6,2,3]))
