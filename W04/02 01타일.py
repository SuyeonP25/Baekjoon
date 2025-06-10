# 01 타일

import sys

N = int(sys.stdin.readline())

prev = 0
curr = 1
next = prev + curr

for i in range(N + 1):
    if i == N: print(curr)

    next = (prev + curr) % 15746
    prev = curr
    curr = next
