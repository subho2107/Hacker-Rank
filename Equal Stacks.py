#!/bin/python3

import os
import sys


#
# Complete the equalStacks function below.
#
def getConsecutiveSum(arr):  # to be done from end to start and 0 is also to be included
    length = len(arr)
    sum = 0
    temp = []
    for data in reversed(arr):
        #print(data)
        temp.append(sum)
        sum += data
    temp.append(sum)
    #print(temp)
    return temp


def doesExist(data, arr):  # to be searched from right to left
    catch = True
    try:
        pos = arr.index(data)
    except:
        catch = False
    return catch

def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    sum_of_h1 = sum(h1)
    sum_of_h2 = sum(h2)
    sum_of_h3 = sum(h3)
    print(sum_of_h1," ",sum_of_h2," ",sum_of_h3)
    smallest = h3
    medium = h3
    largest = h3

    if (sum_of_h1 < sum_of_h2 and sum_of_h1 < sum_of_h3):
        smallest = h1
    if (sum_of_h2 < sum_of_h1 and sum_of_h2 < sum_of_h3):
        smallest = h2
    if (sum_of_h1 > sum_of_h2 and sum_of_h1 > sum_of_h3):
        largest = h1
    if (sum_of_h2 > sum_of_h1 and sum_of_h2 > sum_of_h3):
        largest = h2
    if ((sum_of_h1 > sum_of_h2 and sum_of_h1 < sum_of_h3) or (sum_of_h1 < sum_of_h2 and sum_of_h1 > sum_of_h3)):
        medium = h1
    if ((sum_of_h2 > sum_of_h3 and sum_of_h2 < sum_of_h1) or (sum_of_h2 > sum_of_h3 and sum_of_h2 < sum_of_h1)):
        medium = h2

    cons_sum_s = getConsecutiveSum(smallest)
    cons_sum_l = getConsecutiveSum(largest)
    cons_sum_m = getConsecutiveSum(medium)
    #print(smallest,"<",medium,"<",largest)
    #print(cons_sum_s)
    maximum_height = 0
    for data in reversed(cons_sum_s):
        #print(data)
        if (doesExist(data, cons_sum_m) and doesExist(data, cons_sum_l)):
            maximum_height = data
            break

    return maximum_height




n1N2N3 = input().split()

n1 = int(n1N2N3[0])

n2 = int(n1N2N3[1])

n3 = int(n1N2N3[2])

h1 = list(map(int, input().rstrip().split()))

h2 = list(map(int, input().rstrip().split()))

h3 = list(map(int, input().rstrip().split()))

result = equalStacks(h1, h2, h3)

print(result)
