# 피보나치 수 2

import sys

N = int(sys.stdin.readline())

prev = 0
curr = 1
next = prev + curr

for i in range(N + 1):
    if i == N: print(prev)

    next = prev + curr
    prev = curr
    curr = next
