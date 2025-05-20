import sys
sys.setrecursionlimit(10**8)

N = int(input())
l = []
for i in range(N):
    l.append(list(map(int, input().split())))
visited = [[False] * N for i in range(N)]
safezone = [0]
waterLevel = [0]


def visit(l, i, j, isFirstCheck):
    if visited[i][j]: return
    if l[i][j] > waterLevel[0]:
        if isFirstCheck:
            safezone[0] += 1
        visited[i][j] = True

        if i > 0:
            if not visited[i - 1][j]:
                visit(l, i - 1, j, False)
        if j < N - 1:
            if not visited[i][j + 1]:
                visit(l, i, j + 1, False)
        if i < N - 1:
            if not visited[i + 1][j]:
                visit(l, i + 1, j, False)
        if j > 0:
            if not visited[i][j - 1]:
                visit(l, i, j - 1, False)
    else:
        visited[i][j] = True


max_safezone = 1
for i in range(100):
    waterLevel[0] = i
    safezone[0] = 0

    for j in range(N):
        for k in range(N):
            visited[j][k] = False
    for j in range(N):
        for k in range(N):
            visit(l, j, k, True)

    if max_safezone < safezone[0]:
        max_safezone = safezone[0]

print(max_safezone)
