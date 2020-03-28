#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    hashMap = {0:[], 1:[]}
    for contest in contests:
        luck = contest[0]
        importance = contest[1]
        hashMap[importance].append(luck)
    arrForUnImp = hashMap[0]
    arrImp = sorted(hashMap[1],reverse=True)
    result = 0
    for pos in range(0, len(arrImp)):
        luck = arrImp[pos]
        if pos < k:
            result += luck
        else:
            result -= luck
    result += sum(arrForUnImp)
    return result




if __name__ == '__main__':


    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    print(result)
