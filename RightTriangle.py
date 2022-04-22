def RightTriangle(n:int, s:chr):
    res = ""
    for i in range(n,-1,-1):
        res += s*i + "\n"
    return res