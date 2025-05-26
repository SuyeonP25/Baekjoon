# 제로

import sys

K = int(sys.stdin.readline())
L = list()

for _ in range(K):
    n = int(sys.stdin.readline())
    if n == 0:
        L.pop()
    else:
        L.append(n)

print(sum(L))
