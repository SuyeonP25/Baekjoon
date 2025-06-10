# 듣보잡

import sys

N,M = map(int, sys.stdin.readline().split())
S = set()
res = set()

for _ in range(M):
    name = sys.stdin.readline().strip()
    S.add(name)
for _ in range(N):
    name = sys.stdin.readline().strip()
    if name in S:
        res.add(name)

res = sorted(res)
print(len(res))
for name in res:
    print(name)