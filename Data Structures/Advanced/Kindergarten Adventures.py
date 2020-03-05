"""
PROBLEM LINK:https://www.hackerrank.com/challenges/kindergarten-adventures/problem
"""
#!/bin/python

from __future__ import print_function

import os
import sys
from collections import defaultdict

#
# Complete the solve function below.
#
def solve(t):
    #creating a voting system where the students
    #are voting with whom to start depending on
    #how much time they need and starting from
    #whom will help them. The one with highest votes will
    #be started from
    # Return the ID
    #
    total = len(t)
    Dict = {}
    for i in range(1,total+1):
        Dict[i] = 0
    for student in range(1,total+1):
        if t[student -1] == 0:
            continue
        addPos = student + 1
        subPos = student - t[student - 1] + 1
        if addPos > total:
            addPos = 1
        if subPos <= 0:
            subPos = subPos + total
        Dict[addPos] += 1
        Dict[subPos] -= 1
    
    Max = Dict[1]
    Sum = 0
    MaxPos = 1
    for pos in range(1,total+1):
        Sum += Dict[pos]
        if (Sum > Max):
            Max = Sum
            MaxPos = pos
    
    return MaxPos

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_count = int(raw_input())

    t = map(int, raw_input().rstrip().split())

    id = solve(t)

    fptr.write(str(id) + '\n')

    fptr.close()
