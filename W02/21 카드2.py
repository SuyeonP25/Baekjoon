# 카드2

import sys
import collections

N = int(sys.stdin.readline())
Q = collections.deque([i for i in range(1, N+1)])

while len(Q) != 1:
    Q.popleft()
    Q.rotate(-1)

print(Q.pop())
