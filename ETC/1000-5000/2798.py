# 블랙잭

import itertools

N, M = map(int, input().split())
l = list(map(int, input().split()))

result = 0
C = itertools.combinations(l, 3)
for c in C:
    sumc = sum(c)
    if result < sumc <= M:
        result = sumc
    if result == M:
        break

print(result)
