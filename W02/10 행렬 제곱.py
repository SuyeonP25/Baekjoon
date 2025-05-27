# 행렬 제곱

import sys

N, B = map(int, sys.stdin.readline().split())
A = list()
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))


def mulM(l1: list, l2: list) -> list:
    result = list([0] * N for _ in range(N))
    for i in range(N):
        for j in range(N):
            result[i][j] = sum(l1[i][k] * l2[k][j] for k in range(N)) % 1000

    return result


def powM(l: list, n) -> list:
    if n == 1:
        result = list()
        for i in range(N):
            result.append(list(a % 1000 for a in l[i]))
    else:
        hnl = powM(l, n // 2)
        result = mulM(hnl, hnl)
        if n % 2:
            result = mulM(result, A)
    return result


res = powM(A, B)
for i in range(N):
    for j in range(N):
        print(res[i][j], end=' ')
    print()
