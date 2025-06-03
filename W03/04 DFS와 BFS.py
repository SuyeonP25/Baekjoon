# DFS와 BFS

import sys
import collections

N, M, V = map(int, sys.stdin.readline().split())

Dvisited = set()
Bvisited = set()
ED = dict()

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())

    if A not in ED:
        ED[A] = set()
    ED[A].add(B)
    if B not in ED:
        ED[B] = set()
    ED[B].add(A)

if V in ED:
    # DFS
    Dvisited.add(V)
    count = 1
    print(V, end=' ')
    stack = list()
    s = sorted(ED[V], reverse=True)
    for n in s:
        stack.append(n)

    while count < N and stack:
        next = stack.pop()
        if next not in Dvisited:
            print(next, end=' ')
            Dvisited.add(next)
            count += 1

            s = sorted(ED[next], reverse=True)
            for n in s:
                stack.append(n)
    print()

    # BFS
    Bvisited.add(V)
    count = 1
    print(V, end=' ')
    q = collections.deque()
    s = sorted(ED[V])
    for n in s:
        q.append(n)

    while count < N and q:
        next = q.popleft()
        if next not in Bvisited:
            print(next, end=' ')
            Bvisited.add(next)
            count += 1

            s = sorted(ED[next])
            for n in s:
                q.append(n)
else:
    print(f'{V}\n{V}', end=' ')


