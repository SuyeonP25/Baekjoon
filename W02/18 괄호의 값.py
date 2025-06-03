# 괄호의 값

import sys

S = sys.stdin.readline().rstrip()

stack = list()
score = 0
tmp = 1

for i in range(len(S)):
    if S[i] == '(':
        stack.append(S[i])
        tmp *= 2
    elif S[i] == '[':
        stack.append(S[i])
        tmp *= 3
    elif S[i] == ')':
        if not stack or stack[-1] == '[':
            score = 0
            break
        if S[i - 1] == '(':
            score += tmp
        stack.pop()
        tmp = tmp // 2
    else:
        if not stack or stack[-1] == '(':
            score = 0
            break
        if S[i - 1] == '[':
            score += tmp
        stack.pop()
        tmp = tmp // 3

if stack:
    print(0)
else:
    print(score)
