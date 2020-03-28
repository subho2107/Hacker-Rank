#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    length = len(arr)
    solution = []
    diffArr = []
    if length >= 2:
        for i in range(length-1):
            diffArr.append(arr[i+1]-arr[i])
        minDiff = min(diffArr)
        """for i in range(0, length-1):
            low = i
            high = length - 1
            target = arr[i] + diff
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    solution.append(arr[i])
                    solution.append(arr[mid])
                    break
                elif arr[mid] < target:
                    low += 1
                else:
                    high -= 1"""
        for pos in range(len(diffArr)):
            diff = diffArr[pos]
            if diff == minDiff:
                solution.append(arr[pos])
                solution.append(arr[pos+1])
    return solution



n = int(input())

arr = list(map(int, input().rstrip().split()))
result = closestNumbers(arr)

print(' '.join(map(str, result)))

