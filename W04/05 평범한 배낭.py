# 평범한 배낭

import sys

N, K = map(int, sys.stdin.readline().strip().split())
L = list()

for _ in range(N):
    L.append(list(map(int, sys.stdin.readline().strip().split())))

DP = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])
        if j >= L[i - 1][0]:
            DP[i][j] = max(DP[i][j], DP[i - 1][j - L[i - 1][0]] + L[i - 1][1])

print(DP[N][K])
