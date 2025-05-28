# 히스토그램

import sys

def check(l, r, L):
    if l == r:
        return L[l]
    else:
        # 가운데 영역 직사각형
        mid = (l + r) // 2
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

        # 좌우 영역 직사각형 (재귀)
        leftarea = check(l, mid, L)
        rightarea = check(mid + 1, r, L)

        return max(leftarea, midarea, rightarea)

N = int(sys.stdin.readline())
L = list()
for _ in range(N):
    L.append(int(sys.stdin.readline()))

print(check(0, N - 1, L))
