
def partition(A, start, end):
    #print(A[start:end+1],A)
    equal = [A[start]]
    mid = A[start]
    bigger = []
    smaller = []
    #print(A[start:end+1])
    for num in A[start+1:end+1]:
        if num >= mid:
            bigger.append(num)
        elif num < mid:
            smaller.append(num)
    A[start:len(smaller)+start] = smaller
    #print(A[start:end+1],A)
    A[len(smaller)+start] = mid
    #print(A[start:end+1],A)
    A[len(smaller)+start+1:end+1] = bigger
    #print(A[start:end+1],A)
    #print(" ")
    #print(A[start:end + 1], smaller, bigger,A)
    return len(smaller)+start
def quicksort(A, start, end):
    if start < end:
        pivot = partition(A, start, end)
        #print(pivot)
        quicksort(A, start,pivot-1)
        quicksort(A,pivot+1,end)
        print(A[start:end+1])

n = int(input())
A = list(map(int, input().rstrip().split()))
quicksort(A, 0 , len(A) - 1)
