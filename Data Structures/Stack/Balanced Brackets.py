"""
PROBLEM LINK:https://www.hackerrank.com/challenges/balanced-brackets/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

def doesExist(data, arr):  # to be searched from right to left
    catch = True
    try:
        pos = arr.index(data)
    except:
        catch = False
    return catch

# Complete the isBalanced function below.
def isBalanced(s):
    stack = ""
    length = len(s)
    opening_brackets = ['(', '{', '[']
    closing_brackets = [')', '}', ']']
    check = "YES"
    for pos in range(0, length):
        char = s[pos]
        try:
            if (doesExist(char, opening_brackets)):
                stack += char
            elif (doesExist(char, closing_brackets)):
                if (pos != 0 and opening_brackets.index(stack[len(stack)-1]) == closing_brackets.index(char)):
                    stack = stack[0:(len(stack) - 1)]
                else:
                    check = "NO"
                    break
        except:
            check = "NO"
    if (stack != ""):
        check = "NO"
    return check

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
