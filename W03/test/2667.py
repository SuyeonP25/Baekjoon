# 단지번호붙이기

import sys

sys.setrecursionlimit(int(1e4))

N = int(sys.stdin.readline())
L = list()
for i in range(N):
    L.append(sys.stdin.readline().strip())

visited = [[False] * N for _ in range(N)]
complexL = list()


def check(i, j):
    visited[i][j] = True

    if L[i][j] == '0':
        return 0
    else:
        count = 1

        if i > 0 and not visited[i - 1][j]:
            count += check(i - 1, j)
        if j < N - 1 and not visited[i][j + 1]:
            count += check(i, j + 1)
        if i < N - 1 and not visited[i + 1][j]:
            count += check(i + 1, j)
        if j > 0 and not visited[i][j - 1]:
            count += check(i, j - 1)

        return count


for i in range(N):
    for j in range(N):
        if L[i][j] == '1' and not visited[i][j]:
            complexL.append(check(i, j))

print(len(complexL))
complexL.sort()
for i in complexL:
    print(i)
