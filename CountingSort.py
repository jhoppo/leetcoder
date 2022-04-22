def CountingSort(input):
    keyList = []
    countList = []
    for i in input:
        counts = 0
        for j in input:
            if i == j: counts += 1
        keyList.append(i)
        countList.append(counts)
    print(f"keys: {keyList}")
    print(f"counts: {countList}")
    for i in range(len(input)):
        maxInd = i
        for j in range(len(input)):
            if countList[j] > countList[maxInd]: maxInd = j
            countList[j], countList[maxInd] = countList[maxInd], countList[j]
            keyList[j], keyList[maxInd] = keyList[maxInd], keyList[j]
    return keyList