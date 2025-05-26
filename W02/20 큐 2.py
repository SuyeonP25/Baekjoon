# 큐 2

import sys
import collections

N = int(sys.stdin.readline())
Q = collections.deque()

for _ in range(N):
    insL = list(sys.stdin.readline().split())
    ins = insL.pop(0)
    if ins == "push":
        Q.append(insL.pop())
    elif ins == "pop":
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif ins == "size":
        print(len(Q))
    elif ins == "empty":
        if not Q:
            print(1)
        else:
            print(0)
    elif ins == "front":
        if Q:
            tmp = Q.popleft()
            print(tmp)
            Q.appendleft(tmp)
        else:
            print(-1)
    elif ins == "back":
        if Q:
            tmp = Q.pop()
            print(tmp)
            Q.append(tmp)
        else:
            print(-1)

