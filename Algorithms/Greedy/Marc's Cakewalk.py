#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    calorie = sorted(calorie, reverse=True)
    milesToWalk = 0
    for power in range(0, len(calorie)):
        milesToWalk += 2**power * calorie[power]
    return milesToWalk

if __name__ == '__main__':


    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    print(result)
