# 문자열 폭발

import sys

S = sys.stdin.readline().rstrip()
B = list(sys.stdin.readline().strip())

stack = list()
for s in S:
    stack.append(s)
    if stack[-len(B):] == B:
        for _ in range(len(B)):
            stack.pop()

if stack:
    for s in stack:
        print(s, end='')
    print()
else:
    print('FRULA')
