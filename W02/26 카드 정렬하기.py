# 카드 정렬하기

import heapq
import sys

N = int(sys.stdin.readline())
L = list()
for _ in range(N):
    L.append(int(sys.stdin.readline()))
heapq.heapify(L)

sum = 0

while len(L) > 1:
    a = heapq.heappop(L)
    b = heapq.heappop(L)
    sum += (a + b)
    heapq.heappush(L, a + b)

print(sum)
