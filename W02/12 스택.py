# 스택

import sys

N = int(sys.stdin.readline())
S = list()

for _ in range(N):
    insL = list(sys.stdin.readline().split())
    ins = insL.pop(0)
    if ins == "push":
        S.append(insL.pop())
    elif ins == "pop":
        if S:
            print(S.pop())
        else:
            print(-1)
    elif ins == "size":
        print(len(S))
    elif ins == "empty":
        if not S:
            print(1)
        else:
            print(0)
    elif ins == "top":
        if S:
            print(S[-1])
        else:
            print(-1)
