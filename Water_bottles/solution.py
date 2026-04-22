def waterBottles(num, n):
    output = num
    r = 0
    notEmpty = num
    empty = 0
    while(num//n != 0):
        print(num)
        r = num%n
        q = num//n
        notEmpty = q
        empty = r
        print("Filled with water: ", notEmpty)
        print("Empty: ", empty)
        output += notEmpty
        num = num//n
    return output

print(waterBottles(15, 4))