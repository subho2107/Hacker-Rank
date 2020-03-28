#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'passwordCracker' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY passwords
#  2. STRING loginAttempt
#
check = False
def passwordCracker(loginAttempt):
    global check
    # Write your code here
    if loginAttempt == "":
        check = True
        return ""
    else:
        global hashPass
        global result

        check = False
        possiblePass = ""
        for pos in range(0, len(loginAttempt)):
            char = loginAttempt[pos]
            possiblePass += char
            try:
                temp = hashPass[possiblePass]
                check = True
                return temp +" " + passwordCracker(loginAttempt[pos+1:])
            except:
                continue
        return ""

def generateHash(passArr):
    global  hashPass
    for password in passArr:
        hashPass[password] = password


if __name__ == '__main__':


    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        passwords = input().rstrip().split()

        loginAttempt = input()

        hashPass = {}
        generateHash(passwords)

        result = passwordCracker(loginAttempt)
        # arr = result.rstrip().split()
        if result == "" or check is False:
            result = "WRONG PASSWORD"

        print(result)


