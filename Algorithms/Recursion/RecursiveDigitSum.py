def superDigit(n, k):
    if len(n)*k == 1:
        return n
    else:
        sumOfDig = 0
        for i in n:
            sumOfDig += int(i)
        #print(sumOfDig)
        sumOfDig *= k

        return superDigit(str(sumOfDig),1)


if __name__ == '__main__':
    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    print(result)
