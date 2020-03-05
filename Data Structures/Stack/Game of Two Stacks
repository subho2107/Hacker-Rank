"""
PROBLEM LINK :https://www.hackerrank.com/challenges/game-of-two-stacks/problem
"""
#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#
def twoStacks(x, a, b):
    #
    # Write your code here.
    #
    sum_ = 0
    posOfStack1 = 0
    posOfStack2= 0
    m = len(a)
    n = len(b)
    while(posOfStack1 < m and sum_+a[posOfStack1] <= x ):
        sum_ += a[posOfStack1]
        posOfStack1 += 1
    count = posOfStack1
    while(posOfStack2 < n and posOfStack1 >= 0 ):
        sum_ += b[posOfStack2]
        posOfStack2 += 1
        while(posOfStack1 >0 and sum_ > x):
            posOfStack1 -= 1
            sum_ -= a[posOfStack1]   
        if(sum_ <= x and posOfStack1+posOfStack2 > count):
            count = posOfStack1+posOfStack2
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
