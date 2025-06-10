# 회의실 배정

import sys

N = int(sys.stdin.readline())
I = list()
for _ in range(N):
    I.append(list(map(int, sys.stdin.readline().split())))
I.sort(key=lambda x: (x[1], x[0]))

count = 0
t = -1
for i in I:
    if i[0] >= t:
        count += 1
        t = i[1]

print(count)
