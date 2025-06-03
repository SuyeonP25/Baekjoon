# 연결 요소의 개수

import sys

N, M = map(int, sys.stdin.readline().split())
E = dict()
visited = set()
count = 0
vcount = 0

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    if A not in E:
        E[A] = set()
    E[A].add(B)
    if B not in E:
        E[B] = set()
    E[B].add(A)

for i in E:
    if i not in visited:
        count += 1
        vcount += 1
        visited.add(i)
        stack = list()
        for j in E[i]:
            stack.append(j)

        while stack:
            next = stack.pop()
            if next not in visited:
                vcount += 1
                visited.add(next)
                for j in E[next]:
                    if j not in visited:
                        stack.append(j)

count += N - vcount
print(count)
