# 멀티탭 스케줄링

import sys
import copy

N, K = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))

TS = set()
count = 0

for i in range(K):
    if L[i] in TS:
        continue
    elif len(TS) < N:
        TS.add(L[i])
    else:
        tmpS = copy.deepcopy(TS)
        for j in range(i + 1, K):
            if len(tmpS) == 1:
                break
            if L[j] in tmpS:
                tmpS.remove(L[j])
        TS.remove(tmpS.pop())
        TS.add(L[i])
        count += 1

print(count)
