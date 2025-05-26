# 좌표 정렬하기

import sys

N = int(sys.stdin.readline())
L = list()
for _ in range(N):
    l = tuple(map(int, sys.stdin.readline().split()))
    L.append(l)
L = sorted(L, key=lambda x: (x[0], x[1]))
for x in L:
    print(x[0], x[1])
