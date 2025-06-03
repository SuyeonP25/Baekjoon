# 프린터 큐

import sys
import collections

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    Q = collections.deque(map(int, sys.stdin.readline().split()))

    targeti = M
    count = 0

    while True:
        qfront = Q.popleft()

        if not Q:
            count += 1
            break
        elif qfront < max(Q):
            Q.append(qfront)
            targeti = len(Q) - 1 if targeti == 0 else targeti - 1
        else:
            count += 1
            if targeti == 0:
                break
            targeti = len(Q) - 1 if targeti == 0 else targeti - 1

    print(count)
