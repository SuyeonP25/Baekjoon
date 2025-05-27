# 사냥꾼

import sys

M, N, L = map(int, sys.stdin.readline().split())
Ml = list(map(int, sys.stdin.readline().split()))
Xl = list()
for _ in range(N):
    Xl.append(list(map(int, sys.stdin.readline().split())))
Ml.sort()

count = 0

for x in Xl:
    pl, pr = 0, M - 1
    while pl <= pr:
        mid = (pl + pr) // 2
        dist = abs(Ml[mid] - x[0]) + x[1]
        if dist <= L:
            count += 1
            break
        else:
            if x[0] < Ml[mid]:
                pr = mid - 1
            else:
                pl = mid + 1

print(count)
