def pylons(k, arr):
    noOfTowers = 0
    check = False
    pos = 0
    length = len(arr)
    while pos < length:
        settingAt = pos + k - 1
        check = False
        while True:
            if settingAt >= pos-k+1 and settingAt < length:
                if arr[settingAt] == 1:
                    noOfTowers += 1
                    check = True
                    break
                else:
                    settingAt -= 1
            elif settingAt < pos-k+1:
                break
            # elif settingAt > length:
            #     break
            else:
                settingAt -= 1
        if not check:
            break
        pos = settingAt + k
    if not check:
        return -1
    else:
        return noOfTowers

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    print(result)
"""
7 3
0 1 1 1 0 0 0
"""