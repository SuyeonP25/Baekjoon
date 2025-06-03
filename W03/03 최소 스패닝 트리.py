# 최소 스패닝 트리

# 1. 느려요
# import sys
#
# V, E = map(int, sys.stdin.readline().split())
# AL = list(set() for _ in range(V + 1))
# EL = list()
# mst = set()
# candidate = set()
# cost = 0
#
# for _ in range(E):
#     A, B, C = map(int, sys.stdin.readline().split())
#     EL.append([A, B, C])
#     AL[A].add(B)
#     AL[B].add(A)
#
# EL.sort(key=lambda x: x[2])
#
# # 1번 노드에서 시작
# mst.add(1)
# for i in AL[1]:
#     candidate.add(i)
#
# while len(mst) < V:
#     for e in EL:
#         if (e[0] in candidate and e[1] in mst) or (e[1] in candidate and e[0] in mst):
#             if e[0] in candidate:
#                 candidate.remove(e[0])
#                 mst.add(e[0])
#                 for i in AL[e[0]]:
#                     if i not in mst: candidate.add(i)
#             else:
#                 candidate.remove(e[1])
#                 mst.add(e[1])
#                 for i in AL[e[1]]:
#                     if i not in mst: candidate.add(i)
#
#             EL.remove(e)
#
#             cost += e[2]
#
#             break
#
# print(cost)

import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
EL = [list() for _ in range(V + 1)]

for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    EL[A].append([C, B])
    EL[B].append([C, A])

inmst = [False for _ in range(V + 1)]
cost = 0
count = 0
S = [[0, 1]]

while count < V:
    weight, n = heapq.heappop(S)

    if not inmst[n]:
        inmst[n] = True
        count += 1
        cost += weight
        for e in EL[n]:
            heapq.heappush(S, e)

print(cost)
