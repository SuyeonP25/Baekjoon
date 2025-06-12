# 거스름돈

import sys

N = int(sys.stdin.readline())
DP = [0, sys.maxsize, 1, sys.maxsize, 2]

for i in range(4, N):
    DP.append(min(DP[-5] + 1, DP[-2] + 1))

DP[1] = -1
DP[3] = -1

print(DP[N])