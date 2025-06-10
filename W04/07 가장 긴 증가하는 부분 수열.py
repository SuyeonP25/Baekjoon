# 가장 긴 증가하는 부분 수열

import sys

N = int(sys.stdin.readline())
A = [0] + list(map(int, sys.stdin.readline().split()))

D = [0] * (N + 1)

for i in range(1, N + 1):
    D[i] = 1
    for j in range(1, i):
        if A[i] > A[i - j]:
            D[i] = max(D[i], 1 + D[i - j])

print(max(D))
