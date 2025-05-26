# 나이순 정렬

import sys

N = int(sys.stdin.readline())
L = list()
for _ in range(N):
    l = list(sys.stdin.readline().split())
    l[0] = int(l[0])
    L.append(l)

L = sorted(L, key=lambda x: x[0])

for l in L:
    print(l[0], l[1])