# 이진 검색 트리

import sys

sys.setrecursionlimit(int(1e7))
L = list()


def postodr(start, end):
    if start == end:
        print(f'{L[start]}')
        return
    elif start < end:
        # end+1 = 우측 서브트리 없음
        rsub = end + 1

        for i in range(start + 1, end + 1):
            if L[i] > L[start]:
                rsub = i
                break

        # 후위: 좌, 우, 루트
        postodr(start + 1, rsub - 1)
        postodr(rsub, end)
        print(f'{L[start]}')
    else:
        return

try:
    while True:
        L.append(int(sys.stdin.readline().rstrip()))
except ValueError:
    postodr(0, len(L) - 1)
