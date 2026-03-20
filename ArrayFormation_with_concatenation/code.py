def concatArray(arr, pieces):
    dict = {}
    for piece in pieces:
        dict[piece[0]] = piece
    
    for element in arr:
        if element in dict.keys:
            for values in dict[element]:
                if values not in 

    return True


arr = [15,88]
pieces = [[88],[15]]
print(concatArray(arr, pieces))

