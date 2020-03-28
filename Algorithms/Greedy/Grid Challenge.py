#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):
    rowMax = len(grid)
    colMax = len(grid[0])
    check = "YES"
    for row in range(0, rowMax):
        grid[row] = sorted(list(grid[row]))
    for col in range(0, colMax):
        for row in range(0, rowMax-1):
            if grid[row][col] > grid[row+1][col]:
                check = "NO"
                break

    return  check
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        print(result)