# 공유기 설치

import sys

N, C = map(int, sys.stdin.readline().split())
xl = list()
for _ in range(N):
    xl.append(int(sys.stdin.readline()))
xl.sort()

mind = 1
maxd = xl[-1] - xl[0]
result = 0

while mind <= maxd:
    d = (mind + maxd) // 2
    target = xl[0] + d
    c_count = 1

    for i in range(1, N):
        if xl[i] >= target:
            c_count += 1
            target = xl[i] + d

    if c_count < C:     # d가 작아져야 함
        maxd = d - 1
    else:               # d가 커져도 됨
        mind = d + 1
        result = d

print(result)
