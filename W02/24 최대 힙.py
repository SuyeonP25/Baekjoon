# 최대 힙

import sys
import queue

N = int(sys.stdin.readline())
Q = queue.PriorityQueue()

for _ in range(N):
    ins = int(sys.stdin.readline())
    if ins == 0:
        if Q.empty():
            print(0)
        else:
            print(-Q.get())
    else:
        Q.put(-ins)
