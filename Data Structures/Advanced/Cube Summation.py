"""
PROBLEM LINK:https://www.hackerrank.com/challenges/cube-summation/problem
"""
def toString(a,b,c):
    address = str(a)+" "+str(b)+" "+str(c)
    return address




noOfCases = int(raw_input())
for case in range(0,noOfCases):
    arr = raw_input().split()
    N = int(arr[0])
    M = int(arr[1])
    Dict = {}
    #arrNonZero = []
    for query in range(0,M):
        inputArray = raw_input().split()
        if inputArray[0] == "UPDATE":
            address = toString(inputArray[1],inputArray[2],inputArray[3])
            Dict[address] = inputArray[4]
        elif inputArray[0] == "QUERY":
            _sum_ = 0
            x1 = int(inputArray[1])
            y1 = int(inputArray[2])
            z1 = int(inputArray[3])
            x2 = int(inputArray[4])
            y2 = int(inputArray[5])
            z2 = int(inputArray[6])
            arrIter = Dict.items()
            for element in arrIter:
                arrAdd = element[0].split()
                x = int(arrAdd[0])
                y = int(arrAdd[1])
                z = int(arrAdd[2])
                if(x >= x1 and y >= y1 and z >= z1):
                    if(x <= x2 and y <= y2 and z <= z2):
                        _sum_ += int(element[1])
            
            print _sum_
                        


    
