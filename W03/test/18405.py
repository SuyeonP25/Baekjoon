# 경쟁적 전염

import sys

N, K = list(map(int, sys.stdin.readline().split()))
L = list()

for _ in range(N):
    L.append(list(map(int, sys.stdin.readline().split())))

S, X, Y = map(int, sys.stdin.readline().split())

time = [[0] * N for _ in range(N)]

# 1. 느려요
def check(t, virus):
    for i in range(N):
        for j in range(N):
            if L[i][j] == virus and time[i][j] < t:
                time[i][j] = t
                if i > 0 and time[i - 1][j] < t and L[i - 1][j] == 0:
                    L[i - 1][j] = virus
                    time[i - 1][j] = t
                if j < N - 1 and time[i][j + 1] < t and L[i][j + 1] == 0:
                    L[i][j + 1] = virus
                    time[i][j + 1] = t
                if i < N - 1 and time[i + 1][j] < t and L[i + 1][j] == 0:
                    L[i + 1][j] = virus
                    time[i + 1][j] = t
                if j > 0 and time[i][j - 1] < t and L[i][j - 1] == 0:
                    L[i][j - 1] = virus
                    time[i][j - 1] = t


for s in range(1, S + 1):
    for v in range(1, K + 1):
        check(s, v)
print(L[X - 1][Y - 1])
