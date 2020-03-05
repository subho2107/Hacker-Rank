""
PROBLEM LINK:https://www.hackerrank.com/challenges/jesse-and-cookies/problem
"""
#!/bin/python3

import os
import sys
from heapq import heapify,heappop,heappush

#
# Complete the cookies function below.
#
class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def percolate_down(self, i):
        while(i*2)<= self.size:
            minimum_child = self.minChild(i)
            if self.heap[i] > self.heap[minimum_child]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[minimum_child]
                self.heap[minimum_child] = tmp
            i = minimum_child

    def minChild(self, i):
        if i*2 + 1 > self.size:
            return i*2
        else:
            if self.heap[i*2] < self.heap[2*i + 1]:
                return i*2
            else:
                return i*2 + 1


    def percolate_up(self, i):
        while i//2 > 0:
            if self.heap[i] < self.heap[i//2]:
                tmp = self.heap[i//2]
                self.heap[i//2] = self.heap[i]
                self.heap[i] = tmp
            i = i // 2



    def insert(self, k):
        self.heap.append(k)
        self.size += 1
        self.percolate_up(self.size)

    def delete(self):
        retval = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.percolate_down(1)
        return retval





def cookies(k, A):
    """heapObj = Heap()
    for i in A:
        heapObj.insert(i)
    operations = 0
    while heapObj.heap[1] < k:
        if len(heapObj.heap) <= 2:
            break
        cookie1 = heapObj.delete()
        cookie2 = heapObj.delete()
        cookie3 = cookie1 + (2 * cookie2)
        heapObj.insert(cookie3)
        operations += 1
        if len(heapObj.heap) <= 2:
            break
    if heapObj.heap[1] < k:
        operations = -1"""
    heapify(A)
    operations = 0
    try:
        while A[0] < k:
            operations += 1
            cookie1 = heappop(A)
            cookie2 = heappop(A)
            cookie3 = cookie1 + (2 * cookie2)
            heappush(A, cookie3)
        return operations
    except:
        return -1
    




    return operations

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
