# 괄호

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    S = sys.stdin.readline().rstrip()
    C = []
    valid = True

    for s in S:
        if s == '(':
            C.append(s)
        elif s == ')':
            if not C:
                valid = False
                break
            else:
                C.pop()

    if not C and valid:
        print("YES")
    else:
        print("NO")
