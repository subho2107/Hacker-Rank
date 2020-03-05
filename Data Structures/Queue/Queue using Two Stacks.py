"""
PROBLEM LINK:https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
def enQueue(stackOldestOnTop, query):
    stackOldestOnTop.append(query)

def deQueue(stackOldestOnTop, stackNewestOnTop):
    if len(stackNewestOnTop) != 0:
        stackNewestOnTop.pop()
    else:
        length = len(stackOldestOnTop)
        while length > 0:
            enQueue(stackNewestOnTop, stackOldestOnTop.pop())
            length -= 1
        deQueue(stackOldestOnTop, stackNewestOnTop)


def printHead(stackOldestOnTop, stackNewestOnTop):
    if(len(stackNewestOnTop) != 0):
        print(stackNewestOnTop[len(stackNewestOnTop)-1])
    else:
        length = len(stackOldestOnTop)
        while length > 0:
            enQueue(stackNewestOnTop, stackOldestOnTop.pop())
            length -= 1
        printHead(stackOldestOnTop, stackNewestOnTop)



n = int(input())
stackOldestOnTop = []
stackNewestOnTop = []
for i in range(0, n):
    query = input().split()
    queryNum = int(query[0])
    queryArgs = 0
    if(len(query)==2):
        queryArgs = int(query[1])
    if(queryNum == 1):
        enQueue(stackOldestOnTop, queryArgs)
    elif(queryNum == 2):
        deQueue(stackOldestOnTop, stackNewestOnTop)
    else:
        printHead(stackOldestOnTop, stackNewestOnTop)

