"""
PROBLEM LINK:https://www.hackerrank.com/challenges/simple-text-editor/problem
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())
S= ""
queryArray = []
qaPos = 0
for pos in range(0, t):
    temp = input().split()
    queryNumber = int(temp[0])
    if(queryNumber != 4 and queryNumber != 3):
        queryArray.append(temp)
    queryArgs = 0
    if(queryNumber != 4):
        if(queryNumber != 1):
            queryArgs = int(temp[1])
        else:
            queryArgs = temp[1]
    if(queryNumber == 1):
        S += queryArgs
    elif(queryNumber == 2):
        queryArray[len(queryArray) - 1].append(S)
        S = S[0:len(S)-queryArgs]
    elif(queryNumber == 3):
        print(S[queryArgs-1])
    else:
        undoQueryNum = queryArray[len(queryArray)-1][0]
        undoQueryArgs = queryArray[len(queryArray)-1][1]
        if(undoQueryNum == "1"):
            endPos =len(S) - len(undoQueryArgs)
            S = S[0:endPos]
        else:
            S = queryArray[len(queryArray)-1][2]
        queryArray.pop(len(queryArray)-1)
