# 트리의 부모 찾기

import sys

N = int(sys.stdin.readline())
E = dict()
PN = dict()

for _ in range(N - 1):
    A, B = map(int, sys.stdin.readline().split())
    if A not in E:
        E[A] = set()
    E[A].add(B)
    if B not in E:
        E[B] = set()
    E[B].add(A)

for i in E[1]:
    PN[i] = 1
stack = list(E[1])

while stack:
    next = stack.pop()
    for i in E[next]:
        if i != PN[next]:
            PN[i] = next
            stack.append(i)

for i in range(2, N + 1):
    print(PN[i])
