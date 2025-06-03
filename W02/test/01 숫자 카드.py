# 숫자 카드

import sys

N = int(sys.stdin.readline())
cardL = list(map(int, sys.stdin.readline().split()))

d = dict()

for i in cardL:
    try:
        d[i] += 1
    except KeyError:
        d[i] = 1

M = int(sys.stdin.readline())
targetL = list(map(int, sys.stdin.readline().split()))

for i in targetL:
    try:
        print(d[i], end=' ')
    except KeyError:
        print(0, end=' ')
