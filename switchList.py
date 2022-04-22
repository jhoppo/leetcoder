def switchList(l1,l2):
    for i in range(len(l1)):
        l1[i], l2[i] = l2[i], l1[i]
    return [ l1, l2 ]