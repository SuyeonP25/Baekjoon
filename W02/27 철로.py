# 철로

import sys
import queue

n = int(sys.stdin.readline())
l = list()
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    l.append([a, b] if a < b else [b, a])

d = int(sys.stdin.readline())

l = sorted(l, key=lambda x: x[1])

Q = queue.PriorityQueue()
maxp = 0

for p in l:
    if p[1] - p[0] > d:
        continue

    if Q.empty():
        Q.put(p)
    else:
        while not Q.empty():
            Qleft = Q.get()
            if p[1] - Qleft[0] <= d:
                Q.put(Qleft)
                break
        Q.put(p)

    maxp = max(maxp, Q.qsize())

print(maxp)
