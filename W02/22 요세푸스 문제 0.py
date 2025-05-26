# 요세푸스 문제 0

import sys
import collections

N, K = map(int, sys.stdin.readline().split())
Q = collections.deque([i for i in range(1, N + 1)])

print('<', end='')
while len(Q) != 1:
    Q.rotate(-(K - 1))
    print(f'{Q.popleft()}, ', end='')

print(f'{Q.pop()}>')
