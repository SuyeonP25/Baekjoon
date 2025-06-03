# 문자열 폭발

import sys

S = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

# 1 느려요
# while True:
#     i = S.find(B)
#     if i == -1:
#         break
#     S = S[:i]+S[i+len(B):]

# 2 느려요
# lenB = len(B)
# res = ''
# lenres = 0
#
# for s in S:
#     res = res + s
#     lenres = lenres + 1
#
#     if lenres >= lenB:
#         if res[-lenB:] == B:
#             res = res[:-lenB]

# 3 느려요
stack = list()
for s in S:
    # B와 관련없는 안전 문자
    if s not in B:
        if not stack:
            stack.append(s)
        else:
            stack[-1] = stack[-1] + s
    # B와 관련있는 문자
    else:
        if not stack or B[0] == s:
            stack.append(s)
        else:
            stack[-1] = stack[-1] + s
            if stack[-1] == B:
                stack.pop()

if stack:
    for s in stack:
        print(s, end='')
    print()
else:
    print('FRULA')
