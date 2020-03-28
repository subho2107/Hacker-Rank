def getMinimumCost(k, c):
    c.sort()
    if k == len(c):
        return sum(c)
    else:
        result = 0
        length = len(c)
        if length % k == 0:
            cSplitByKArrays = [[] for _ in range(int(length/k))]
            for pos in range(length):
                toInsertAt = int(pos/k)
                cSplitByKArrays[toInsertAt].append(c[pos])
        else:
            cSplitByKArrays = [[] for _ in range(int(length / k)+1)]
            pos = int(length/k)
            count = 0
            for num in reversed(c):
                if count == k:
                    pos -= 1
                    count = 0
                cSplitByKArrays[pos].append(num)
                count += 1

        #print(cSplitByKArrays)
        length = len(cSplitByKArrays)
        prevBought = 0
        for arr in reversed(cSplitByKArrays):
            for num in arr:
                result += (prevBought+1)*num
            prevBought += 1
        return result



if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    print(minimumCost)
