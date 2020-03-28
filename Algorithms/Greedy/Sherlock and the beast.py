def decentNumber(n):
    rem3 = n % 3
    result = ""
    rem5 = n % 5
    if rem3 == 0:
        result = "5"*n
    elif n < 3:
        result = "-1"
    else:
        div3 = int(n / 3)
        while True:
            if (n - (div3 * 3)) % 5 == 0 or div3 == 0:
                break
            div3 -= 1
        if div3 <= 0:
            if n % 5 == 0:
                result = "3"*n
            else:
                result = "-1"
        else:
            noOf5 = div3 * 3
            result = "5"*noOf5 + "3"*(n - noOf5)
    print(result)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)