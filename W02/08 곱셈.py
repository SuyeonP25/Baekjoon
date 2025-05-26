# 곱셈

import sys

A, B, C = map(int, sys.stdin.readline().split())

res = 1
B2b = f"{B:b}"
AmC = [A % C]

for i in range(1, len(B2b)):
    AmC.append(AmC[i - 1] * AmC[i - 1] % C)

for i in range(len(B2b)):
    if B2b[i] == '1':
        res *= AmC[len(B2b) - i - 1]
        res = res % C

print(res)
