# 이항 계수

import sys

N, K = map(int, sys.stdin.readline().split())

u = 1
for i in range(K):
    u *= N - i
d = 1
for i in range(K):
    d *= i + 1

print(u // d)
