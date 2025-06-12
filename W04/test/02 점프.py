# 점프

import sys

N = int(sys.stdin.readline())
board = list()
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

count = list([0] * N for _ in range(N))
count[0][0] = 1

for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            continue
        if j + board[i][j] < N:
            count[i][j + board[i][j]] += count[i][j]
        if i + board[i][j] < N:
            count[i + board[i][j]][j] += count[i][j]

print(count[N - 1][N - 1])
