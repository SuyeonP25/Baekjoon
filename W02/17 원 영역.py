# 원 영역

import sys

N = int(sys.stdin.readline())
CL = list()
for _ in range(N):
    c = list(map(int, sys.stdin.readline().split()))
    CL.append((c[0] - c[1], -1))
    CL.append((c[0] + c[1], 1))
CL = sorted(CL, key=lambda x: (x[0], -x[1]))

aCnt = 1
stack = list()

for c in CL:
    # 원 왼쪽점
    if c[1] == -1:
        stack.append(c)
        continue

    # 원 오른쪽점
    else:
        rsum = 0

        while stack:
            prev = stack.pop()

            if prev[1] == 0:
                rsum += prev[0]
            elif prev[1] == -1:
                width = c[0] - prev[0]

                if width == rsum:
                    aCnt += 2
                else:
                    aCnt += 1

                stack.append((width, 0))
                break

print(aCnt)
