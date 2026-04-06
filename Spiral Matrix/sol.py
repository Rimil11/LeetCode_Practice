def spiralMatrix(input):

    output = []
    c = len(input[0])
    r = len(input)
    for i in range(r):
        if(i == 0):
            output.extend(input[i])

        elif(i == r-1):    
            output.extend(input[i].reverse())
        else:
            print(input[-1])
a = [[3,4,5], [3,1,4]]
spiralMatrix(a)