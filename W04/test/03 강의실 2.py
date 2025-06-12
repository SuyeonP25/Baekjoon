# 강의실 2

import sys

N = int(sys.stdin.readline())
L = list()
for _ in range(N):
    n, start, end = map(int, sys.stdin.readline().split())
    L.append([n, start, end])

L.sort(key=lambda x: (x[2], x[1]))

CD = [sys.maxsize]
LD = dict()
count = 0

for l in L:
    cfound = False

    for i in range(count):
        if l[1] > CD[i]:
            LD[l[0]] = i
            CD[i] = l[2]
            cfound = True
            break

    if cfound:
        continue
    else:
        count += 1
        CD.append(l[2])
        LD[l[0]] = count

print(count)
for i in range(1, N + 1):
    print(LD[i])
