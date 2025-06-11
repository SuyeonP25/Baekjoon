# 점프

import sys

N, M = map(int, sys.stdin.readline().split())
MS = set()
for _ in range(M):
    MS.add(int(sys.stdin.readline()))

DP = list(dict() for _ in range(N + 1))

DP[1][0] = 0

for i in range(1, N + 1):
    for x, cnt in DP[i].items():
        for d in [-1, 0, 1]:
            v = x + d
            nxt = i + v
            if v > 0 and nxt <= N and nxt not in MS:
                if v in DP[nxt]:
                    DP[nxt][v] = min(DP[nxt][v], cnt + 1)
                else:
                    DP[nxt][v] = cnt + 1

if not DP[N]:
    print(-1)
else:
    print(min(DP[N].values()))
