# 히스토그램에서 가장 큰 직사각형

import sys

def check(l, r, L):
    if l == r:
        return L[l]
    else:
        mid = (l + r) // 2

        leftarea = check(l, mid, L)
        rightarea = check(mid + 1, r, L)

        pl, pr = mid, mid + 1
        width = 2
        height = min(L[pl], L[pr])
        midarea = width * height

        while pl > l or pr < r:
            plh = L[pl - 1] if l < pl else -1
            plr = L[pr + 1] if pr < r else -1

            if plh < plr:
                height = min(height, plr)
                pr += 1
            else:
                height = min(height, plh)
                pl -= 1

            width += 1
            midarea = max(midarea, width * height)

        return max(leftarea, midarea, rightarea)

while True:
    L = list(map(int, sys.stdin.readline().split()))
    n = L.pop(0)
    if n == 0:
        break

    print(check(0, n - 1, L))
