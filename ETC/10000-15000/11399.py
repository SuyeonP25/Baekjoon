# ATM

import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
L.sort()

ans = 0
for i in range(1, N + 1):
    ans += sum(L[:i])

print(ans)
