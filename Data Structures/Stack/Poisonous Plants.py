"""
PROBLEM LINK:https://www.hackerrank.com/challenges/poisonous-plants/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants(p):
    day = 0
    stackArr = []
    pos = 0
    stackArr.append([])
    stackArr[0].append(p[0])
    for i in range(1, len(p)):
        if (p[i] <= p[i - 1]):
            stackArr[pos].append(p[i])
        else:
            pos += 1
            stackArr.append([])
            stackArr[pos].append(p[i])
    length = len(stackArr)
    while len(stackArr) != 1:

            i = 1
            while (i < len(stackArr)):
                stackArr[i].pop(0)

                if (len(stackArr[i]) != 0):

                    if (stackArr[i][0] <= stackArr[i - 1][len(stackArr[i - 1]) - 1]):
                        stackArr[i - 1] += stackArr[i]
                        stackArr.pop(i)
                        i -= 1

                else:
                    stackArr.pop(i)
                    i -= 1
                if (i >= len(stackArr) - 1):
                    break
                i += 1
            day += 1
    return day
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
