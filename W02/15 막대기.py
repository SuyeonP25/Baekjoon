# 막대기

import sys

N = int(sys.stdin.readline())
L = list()

for _ in range(N):
    L.append(int(sys.stdin.readline()))

resL = list()
for l in L:
    if not resL or resL[-1] > l:
        resL.append(l)
    else:
        while True:
            if resL and resL[-1] <= l:
                resL.pop()
            else:
                resL.append(l)
                break

print(len(resL))
