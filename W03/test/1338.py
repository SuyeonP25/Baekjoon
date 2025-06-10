# 바닥 장식

import sys

N, M = map(int, sys.stdin.readline().split())

L = list()
for _ in range(N):
    L.append(sys.stdin.readline().strip())

visited = [[False] * M for _ in range(N)]
count = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = True
            count += 1

            if L[i][j] == '|':
                for k in range(i, N):
                    if L[k][j] == '|':
                        visited[k][j] = True
                    elif L[k][j] == '-':
                        break

            if L[i][j] == '-':
                for k in range(j, M):
                    if L[i][k] == '-':
                        visited[i][k] = True
                    elif L[i][k] == '|':
                        break

print(count)
