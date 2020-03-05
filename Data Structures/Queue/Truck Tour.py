"""
PROBLEM LINK:https://www.hackerrank.com/challenges/truck-tour/problem
"""
#!/bin/python3

import os
import sys

#
# Complete the truckTour function below.
#
def truckTour(petrolpumps):
    #
    # Write your code here.
    #
    petrol = 0
    startpoint = 0
    #extraRequired = 0
    for i in range(0, len(petrolpumps)):
        petrol += petrolpumps[i][0] - petrolpumps[i][1]
        if petrol < 0:
            startpoint = i+1
            #extraRequired = petrol
            petrol = 0
    return startpoint

    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
