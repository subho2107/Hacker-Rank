"""
 PROBLEM LINK:https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
"""
#!/bin/python3

import math
import os
import random
import re
import bisect

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    count = 0
    arr = []
    hashMap = {}
    maxExpense = max(expenditure)
    for expense in range(0,maxExpense+1):
        hashMap.setdefault(expense, 0)
    for expense in expenditure[0:d]:
        hashMap[expense] += 1
    mid = d//2
    for i in range(d,len(expenditure)):
        #print(hashMap)
        if i != d:
            # if expenditure[i-1] not in hashMap:
            #         hashMap.setdefault(expenditure[i-1],1)
            # else:
            hashMap[expenditure[i-1]] += 1
            prevExpense = expenditure[i-d-1]
            #print(prevExpense,i,i-d)
            hashMap[prevExpense] -= 1
            # if hashMap[prevExpense] == 0:
            #     del hashMap[prevExpense]
        if d % 2 == 0:
            median = 0
            elements = 0
            checkFirst = False
            for hash in hashMap:
                elements += hashMap[hash]
                if elements == mid:
                    median += hash
                    #print(hash)
                    checkFirst = True
                if elements >= mid + 1 and checkFirst:
                    median += hash
                    #print(hash)
                    break
                elif elements > mid:
                    median += 2 * hash
                    #print(hash,hash)
                    break
            median = median / 2
        else:
            median = 0
            elements = 0
            for hash in hashMap:
                elements += hashMap[hash]
                if elements >= mid + 1:
                    median = hash
                    #print(hash)
                    break
        #print(median,elements)
        if expenditure[i] >= median * 2:

            count += 1
            #print(expenditure[i], arr, median)
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
