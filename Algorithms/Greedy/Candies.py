def candies(arr):
    length = len(arr)
    candyArr = [1 for _ in range(0, length)]

    for pos in range(1, length):
        if arr[pos] > arr[pos-1]:
            candyArr[pos] = candyArr[pos-1]+1

    for pos in range(length-2 , -1, -1):
        #print(pos)
        if arr[pos] > arr[pos+1] and candyArr[pos] <= candyArr[pos+1]:
            candyArr[pos] = candyArr[pos+1]+1

    return sum(candyArr)

if __name__ == '__main__':
    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(arr)

    print(result)
