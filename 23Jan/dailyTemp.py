# Brute Force

def dailyTemp(temps):
    result = []
    n = len(temps)
    print(n)
    for i in range(0, n):
        # print(f"{i}th outer loop")
        if(i==n-1):
            result.append(count)
            continue
        count = 0
        for j in range(i+1, n):
            # print(f"{j}th inner loop")
            if(temps[i]<temps[j]):
                count+=1
                result.append(count)
                break
            
            elif(count==0 and j==n-1):
                result.append(0)
            
            else:
                count+=1
    return result

print(dailyTemp([73,74,75,71,69,72,76,73]))


# Effiicient Method

def effDailyTemp(temps):
    stack = []
    n = len(temps)
    result = [0]*n

    i = n-1

    while(i>=0):
        if stack:
            print("Top: ", stack[-1])
            print("Stack: ", stack)
        else:
            print("[]")
        print("Current element: ", temps[i])
        while stack and temps[stack[-1]]<temps[i]:
            stack.pop()
        if(stack):
            result[i] = stack[-1] - i
        stack.append(i)

        i-=1

    return result

print(effDailyTemp([73,74,75,71,69,72,76,73]))
