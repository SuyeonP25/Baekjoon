# 가운데를 말해요

import sys
import heapq

N = int(sys.stdin.readline())
minheap = list()
maxheap = list()

tmp = int(sys.stdin.readline())
print(tmp)
heapq.heappush(maxheap, -tmp)

for i in range(1, N):
    if len(minheap) == len(maxheap):
        heapq.heappush(maxheap, -int(sys.stdin.readline()))
    else:
        heapq.heappush(minheap, int(sys.stdin.readline()))

    minroot = heapq.heappop(minheap)
    maxroot = -heapq.heappop(maxheap)

    if minroot < maxroot:
        minroot, maxroot = maxroot, minroot

    heapq.heappush(minheap, minroot)
    heapq.heappush(maxheap, -maxroot)

    print(-maxheap[0])
