


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lilysHomework function below.
def swap(A,i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
def lilysHomework(arr):
    count = 0
    newArr = sorted(arr)
    for i in range(len(arr)):
        tempArr = arr[i+1:]
        minPos = i+ 1 +tempArr.index(min(tempArr))
        swap(arr,i,minPos)
        count += 1
        if arr == newArr:
            break
    return count


n = int(input())

arr = list(map(int, input().rstrip().split()))

result = lilysHomework(arr)

print(result)