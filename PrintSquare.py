def PrintSquare(n,s):
    emptyArray = [ [ '' for i in range(n) ] for i in range(n) ]
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 :
                emptyArray[i][j] = s
            elif j == 0 or j == n-1 :
                emptyArray[i][j] =s
            else:
                emptyArray[i][j] = " "
    return emptyArray