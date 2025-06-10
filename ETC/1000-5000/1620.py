# 나는야 포켓몬 마스터 이다솜

import sys

N,M = map(int, sys.stdin.readline().split())
L = [' ']
D = dict()
for i in range(1,N+1):
    name = sys.stdin.readline().rstrip()
    L.append(name)
    D[name] = i

for _ in range(M):
    ins = sys.stdin.readline().rstrip()
    if ins.isdigit():
        print(L[int(ins)])
    else:
        print(D[ins])