#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the powerSum function below

def powerSum(X, N, num):
    if pow(num, N) < X:
        return powerSum(X,N,num+1) + powerSum(X-pow(num, N),N,num+1)
    elif pow(num, N) == X:
        return 1
    else:
        return 0



if __name__ == '__main__':
    X = int(input())

    N = int(input())

    result = powerSum(X, N, 1)

    print(result)

