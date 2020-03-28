def maxMin(k, arr):
    arr.sort()
    length = len(arr)
    minDiff = arr[-1] - arr[0]
    for pos in range(0, length - k + 1):
        diff = arr[pos+k-1] - arr[pos]
        if diff < minDiff:
            minDiff = diff
    return minDiff


if __name__ == '__main__':
    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    print(result)
