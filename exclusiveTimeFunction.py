
def exclusiveTime(n, logs):

    stack = []
    result = []
    top = None
    prevTime = 0
    for log in logs:
        process_id, status, time = log.split(":")
        time = int(time)
        process_id = int(process_id)
        if status == "end" and int(stack.index(top)) == process_id :
            
            prevTime = time - top - prevTime + 1
            result.append(prevTime)
            stack.pop()
            print("PrevTime: ", prevTime)
        else:
            print("Else")
            stack.append(time)
            print("last pushed: ", top)
            top = time
            
        print("Stack: ", stack)
        print("Result: ", result)
    print("Final Result: ", result)
    return (result[::-1])


# print("Final result: ", exclusiveTime(["0:start:0","1:start:2","1:end:5","0:end:6"]))
exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"])
        
            
            