def checkForSunnyDays(hashPosAndIsSunny, positions, coverage):
    # hashCloudPres = {}
    for pos in range(len(positions)):
        distanceCov = coverage[pos]
        cloudAt = positions[pos]
        start = cloudAt - distanceCov
        end = cloudAt + distanceCov
        if start<0:
            start = 1
        for cloud in range(start, end+1):
            # hashCloudPres[cloud] = "Present"
        hashPosAndIsSunny[start] += 1

            if cloud in hashPosAndIsSunny:
                hashPosAndIsSunny[cloud] = False
    #print(hashPosAndIsSunny)
    # print(hashCloudPres)
    #print(hashPopulation)
    # for pos in hashPosAndPop:
    #     if pos not in hashCloudPres:
    #         population = hashPosAndPop[pos]
    #         hashPopulation[population][1] = True
    # return hashPopulation


def findClouds(posWithMax, cloudsPos, cloudRange):
    maxPos = 0
    maxRange = cloudRange[0]
    length = len(cloudsPos)
    for pos in range(1,length):
        distanceCov = cloudRange[pos]
        cloudAt = cloudsPos[pos]
        start = cloudAt - distanceCov
        end = cloudAt + distanceCov
        if start<0:
            start = 1
        if posWithMax >= start and posWithMax <= end:
            if distanceCov > maxRange:
                maxRange = distanceCov
                maxPos = pos
    #print(maxRange,"max range",posWithMax)
    return maxPos






def maximumPeople(p, x, y, r):
    # Return the maximum number of people that will be in a sunny town after removing exactly one cloud.
    hashPopulation = {}
    for pos in range(len(p)):
        population = p[pos]
        position = x[pos]
        if position in hashPopulation:
            hashPopulation[position] += population
        else:
            hashPopulation[position] = population
    # print("population", p)
    # print("pos",x)
    # print(hashPopulation)
    hashPosAndIsSunny = {}
    for pos in range(len(x)):
        position = x[pos]
        hashPosAndIsSunny[position] = 0
    #print(hashPosAndIsSunny,"before")

    checkForSunnyDays(hashPosAndIsSunny, y, r)
    #print(hashPosAndIsSunny,"after")

    arrPopulation = [(a,b) for a,b in hashPopulation.items()]
    arrPopulation.sort(key = lambda x: x[1],reverse = True)
    posWithMaxPop = 0
    for tup in arrPopulation:
        if not hashPosAndIsSunny[tup[0]] :
            posWithMaxPop = tup[0]
            break
    #print(arrPopulation,posWithMaxPop)
    maxCloudPos = findClouds(posWithMaxPop,y,r)
    #print(maxCloudPos)
    y.pop(maxCloudPos)
    r.pop(maxCloudPos)
    tempHash = {}
    for pos in hashPosAndIsSunny:
        tempHash[pos] = True
    checkForSunnyDays(tempHash,y,r)
    maxPopulation = 0
    for pos in tempHash:
        if tempHash[pos]:
            maxPopulation += hashPopulation[pos]

    return maxPopulation






if __name__ == '__main__':
    n = int(input())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    print(result)
