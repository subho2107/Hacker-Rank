def solution(a):
    m = {}
    print(a)
    for i in range(len(a)):
        m[a[i]] = i

    sorted_a = sorted(a)
    ret = 0
    print(len(a))
    for i in range(len(a)):
        if a[i] != sorted_a[i]:
            ret += 1

            ind_to_swap = m[sorted_a[i]]
            m[a[i]] = m[sorted_a[i]]
            a[i], a[ind_to_swap] = sorted_a[i], a[i]
    return ret


input()
a = [int(i) for i in input().split(' ')]

asc = solution(list(a))
print(a)
desc = solution(list(reversed(a)))
print(asc, desc)