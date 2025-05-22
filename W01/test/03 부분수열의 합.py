# 부분수열의 합

import itertools

N, S = map(int, input().split())
l = list(map(int, input().split()))
cnt = 0

for i in range(N):
    C = itertools.combinations(range(N), i + 1)
    for c in C:
        if sum(l[a] for a in c) == S:
            cnt += 1

print(cnt)
