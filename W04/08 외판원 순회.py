# 외판원 순회

import sys

N = int(input())
E = list()
for i in range(N):
    E.append(list(map(int, input().split())))

DP = [[sys.maxsize] * 2 ** N for i in range(N)]
DP[0][1] = 0

for A in range(2 ** N):
    for prev in range(N):
        if not (A & (2 ** prev)):
            continue
        for next in range(N):
            if A & (2 ** next):
                continue
            if E[prev][next] == 0:
                continue
            nextA = A | (2 ** next)
            DP[next][nextA] = min(DP[next][nextA], DP[prev][A] + E[prev][next])

mind = sys.maxsize
for i in range(1, N):
    if E[i][0] != 0:
        mind = min(mind, DP[i][2 ** N - 1] + E[i][0])
print(mind)
