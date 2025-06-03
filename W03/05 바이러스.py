# 바이러스

import sys

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
ED = dict()
visited = set()
stack = list()

for _ in range(E):
    A, B = map(int, sys.stdin.readline().split())
    if A not in ED:
        ED[A] = set()
    ED[A].add(B)
    if B not in ED:
        ED[B] = set()
    ED[B].add(A)

# 1번과 아무도 연결 안 됨
if 1 not in ED:
    print(0)
    exit()

visited.add(1)
for i in ED[1]:
    stack.append(i)

while stack:
    next = stack.pop()
    if next not in visited:
        visited.add(next)
        for i in ED[next]:
            if i not in visited:
                stack.append(i)

print(len(visited) - 1)
