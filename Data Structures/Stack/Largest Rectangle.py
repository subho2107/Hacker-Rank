"""
PROBLEM LINK:https://www.hackerrank.com/challenges/largest-rectangle/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    stack = []
    maxArea = -1
    i = 0
    while(i < len(h)):
        if(len(stack)==0 or h[i] >= h[stack[len(stack)-1]]):
            stack.append(i)
            i += 1
        else:
            area = 0
            top = stack.pop()
            if(len(stack) == 0):
                area = h[top] * i
            else:
                area = h[top] * (i - stack[len(stack)-1] - 1)
            if(area > maxArea):
                maxArea = area
    area = 0
    while(len(stack) != 0):
        top = stack.pop()
        if (len(stack) == 0):
            area = h[top] * i
        else:
            area = h[top] * (i - stack[len(stack) - 1] - 1)
        if (area > maxArea):
            maxArea = area
    return maxArea

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
