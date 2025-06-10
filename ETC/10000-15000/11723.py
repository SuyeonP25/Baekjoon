# 집합

import sys

M = int(sys.stdin.readline())
S = set()
for _ in range(M):
    ins = sys.stdin.readline()

    if ins[:2] == "ad":
        n = int(ins.split()[1])
        S.add(n)
    elif ins[:2] == "re":
        n = int(ins.split()[1])
        if n in S:
            S.remove(n)
    elif ins[:2] == "ch":
        n = int(ins.split()[1])
        if n in S:
            print(1)
        else:
            print(0)
    elif ins[:2] == "to":
        n = int(ins.split()[1])
        if n in S:
            S.remove(n)
        else:
            S.add(n)
    elif ins[:2] == "al":
        S = set(range(1,21))
    elif ins[:2] == "em":
        S = set()

