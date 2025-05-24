# 두 용액

import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
L.sort()

abs_min = 2000000000
targetl, targetr = 0, 0
pl, pr = 0, N - 1
while pl < pr:
    if abs(L[pl] + L[pr]) < abs_min:
        targetl, targetr = L[pl], L[pr]
        abs_min = abs(L[pl] + L[pr])
    if L[pl] + L[pr] > 0:  # 큰 수 낮추기
        pr -= 1
    elif L[pl] + L[pr] < 0:  # 작은 수 높이기
        pl += 1
    else:  # L[pl] + L[pr] == 0
        break

print(targetl, targetr)
