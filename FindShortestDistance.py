def FindSohrtestDistance(dots):
    shortest = 10**4
    res = []
    while len(dots) > 0:
        res.append(dots.pop(0))
        for i in dots:
            curDist = (((res[-1][0] - i[0])**2) + ((res[-1][1] - i[1])**2))**0.5
            print(f"{res[-1]},{i}: {curDist}")
            if curDist < shortest:
                shortest = curDist
                ret = [ res[-1], i]
    return f"{ret}: {shortest} is the shortest points"