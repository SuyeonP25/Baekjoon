# 가장 가까운 두 점

import sys
import math

N = int(sys.stdin.readline())
P = list()
for _ in range(N):
    P.append(list(map(int, sys.stdin.readline().split())))
P.sort()


def pointdist(l, r):
    return (l[0] - r[0]) ** 2 + (l[1] - r[1]) ** 2


def minpointdist(l, r):
    if l == r:
        return math.inf
    elif l + 1 == r:
        return pointdist(P[l], P[r])
    else:
        mid = (l + r) // 2

        minleft = minpointdist(l, mid)
        minright = minpointdist(mid, r)
        mind = min(minleft, minright)

        possiblep = list()

        for i in range(l, r + 1):
            if (P[mid][0] - P[i][0]) ** 2 < mind:
                possiblep.append(P[i])

        possiblep.sort(key=lambda x: x[1])

        for i in range(len(possiblep) -1):
            for j in range(i+1, len(possiblep)):
                if (possiblep[i][1] - possiblep[j][1]) ** 2 < mind:
                    mind = min(mind, pointdist(possiblep[i], possiblep[j]))
                else:
                    break

        return mind


print(minpointdist(0, N - 1))
