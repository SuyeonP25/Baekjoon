# 크게 만들기

import sys

N, K = map(int, sys.stdin.readline().split())
n = sys.stdin.readline().rstrip()
result = list()
k = K

for i in n:
    while k > 0 and result and result[-1] < i:
        result.pop()
        k -= 1
    result.append(i)

while len(result) != N - K:
    result.pop()

for r in result:
    print(r, end='')
