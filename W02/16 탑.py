# 탑

import sys

N = int(sys.stdin.readline())
L = [0] + list(map(int, sys.stdin.readline().split()))

result = [0] * (N + 1)
iS = list()
hS = list()

for i in range(N, 0, -1):
    if not hS or hS[-1] > L[i]:
        hS.append(L[i])
        iS.append(i)
    else:
        while hS and hS[-1] < L[i]:
            hS.pop()
            result[iS.pop()] = i
        hS.append(L[i])
        iS.append(i)

for i in range(1, N + 1):
    print(result[i], end=' ')
