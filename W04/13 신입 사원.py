# 신입 사원

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    L = list()
    for _ in range(N):
        L.append(list(map(int, sys.stdin.readline().split())))

    L.sort(key=lambda x:(x[0],x[1]))
    count = 0
    smax = sys.maxsize
    for l in L:
        if l[1] < smax:
            count += 1
            smax = l[1]

    print(count)

