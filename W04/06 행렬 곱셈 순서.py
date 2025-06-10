# 행렬 곱셈 순서

import sys

N = int(sys.stdin.readline())
L = list()
for _ in range(N):
    L.append(list(map(int, sys.stdin.readline().split())))

DP = [[0] for _ in range(N)]

for l in range(2, N + 1):
    for start in range(N - l + 1):
        end = start + l - 1
        DP[start].append(min(
            DP[start][mid - start] + DP[mid + 1][end - mid - 1] + L[start][0] * L[mid][1] * L[end][1]
            for mid in range(start, end)))

print(DP[0][N - 1])
