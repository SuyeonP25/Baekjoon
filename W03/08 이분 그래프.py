# 이분 그래프

import sys

K = int(sys.stdin.readline())

for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    ED = dict()
    C = dict()
    isbi = True

    for _ in range(E):
        A, B = map(int, sys.stdin.readline().split())
        if A not in ED:
            ED[A] = set()
        ED[A].add(B)
        if B not in ED:
            ED[B] = set()
        ED[B].add(A)

    for i in range(1, V + 1):
        if not isbi:
            break

        if i not in ED or i in C:
            continue

        C[i] = 1
        for j in ED[i]:
            C[j] = -C[i]
        stack = list(ED[i])

        while stack and isbi:
            next = stack.pop()
            for j in ED[next]:
                if j not in C:
                    C[j] = -C[next]
                    stack.append(j)
                elif C[j] == C[next]:
                    isbi = False
                    break

    if isbi:
        print("YES")
    else:
        print("NO")
