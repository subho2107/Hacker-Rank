cntSwap = 0
def swap(A, i, j):
    global cntSwap
    dup = A[i]
    A[i] = A[j]
    A[j] = dup
    cntSwap += 1


def partition(A, start, end):
    #print(end)
    pivot = A[end]
    i = start-1
    for j in range(start, end):
        if A[j] <= pivot:
            i += 1
            swap(A, i, j)
    swap(A, i+1, end)
    #print(A)
    return i+1

"""def partition(A, start, end):
    pivot = A[start]
    i = start
    for j in range(start+1, end+1):
        if A[j] <= pivot:
            i += 1
            swap(A, i, j)
    swap(A, i, start)
    print(A)
    return i"""
#5 1 8 3 7 9 2
#5 1 3 8 7 9 2
#5 1 3 2 7 9 8
"""
2 1 3 5 7 9 8
1 2 3 5 7 9 8
1 2 3 5
"""
def quickSort(A, start, end):
    if start < end:
        partitioningPos = partition(A, start, end)
        quickSort(A, start,partitioningPos-1)
        quickSort(A, partitioningPos+1, end)

#global cntSwap
n = int(input())
arr = list(map(int, input().rstrip().split()))
quickSort(arr, 0, len(arr) - 1)
#print(arr)
print(cntSwap)