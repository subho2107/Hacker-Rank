#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    minDiff = arr[1] - arr[0]
    for pos in range(1, len(arr)-1):
        diff = arr[pos+1] - arr[pos]
        if diff < minDiff:
            minDiff = diff
    return minDiff


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(result)
