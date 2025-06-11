# 아침 산책

import sys

N = int(sys.stdin.readline())
V = ' ' + sys.stdin.readline()
E = dict()

visited = set()
count = 0

for _ in range(N - 1):
    A, B = map(int, sys.stdin.readline().split())
    if A not in E:
        E[A] = set()
    E[A].add(B)
    if B not in E:
        E[B] = set()
    E[B].add(A)

    if V[A] == '1' and V[B] == '1':
        count += 2

for i in range(1, N + 1):
    if V[i] == '1' or i in visited: continue
    visited.add(i)

    outcnt = 0
    tmpvisited = {i}
    stack = list()
    for e in E[i]:
        if V[e] == '1':
            outcnt += 1
        else:
            stack.append(e)

    while stack:
        next = stack.pop()
        visited.add(next)
        tmpvisited.add(next)

        if V[next] == '1':
            outcnt += 1
        else:
            for e in E[next]:
                if e not in tmpvisited:
                    stack.append(e)

    count += outcnt * (outcnt - 1)

print(count)
