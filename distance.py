def distance(A:list, B:list) -> float:
    """
    Calculate the distance of 2 points
    :param A: [x1,y1]
    :param B: [x2,y2]
    :return: float, which represent the distance of line A-B
    """
    dx = (A[0]-B[0]) ** 2
    dy = (A[1]-B[1]) ** 2
    C = (dx+dy) ** 0.5
    return C