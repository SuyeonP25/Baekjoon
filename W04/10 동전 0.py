# 동전 0

import sys

N, K = map(int, sys.stdin.readline().split())
L = list()
for _ in range(N):
    L.append(int(sys.stdin.readline()))
L.reverse()

target = K
count = 0

for l in L:
    if l <= target:
        count += target // l
        target %= l
    if target == 0:
        break

print(count)
