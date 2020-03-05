"""
PROBLEM LINK:https://www.hackerrank.com/challenges/countingsort4/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    length = len(arr)
    mid = length // 2
    
    """
        Now I will link a list to each number. The list will contain the strings that
        are linked to the number
    """
    hashSorter = {}
    for num in range(0, 101):
        hashSorter[num] = []

    for pos in range(length):
        query = arr[pos]
        number = int(query[0])
        string = query[1]
        toInsert = ""
        if pos < mid:
            toInsert = '-'
        else:
            toInsert = string
        hashSorter[number].append(toInsert)

    for num in hashSorter:
        if hashSorter[num] != []:
            print(' '.join(hashSorter[num]), end = " ")

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
