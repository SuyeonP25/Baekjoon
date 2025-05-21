# 오븐 시계

A, B = map(int, input().split())
C = int(input())

h, m = C // 60, C % 60
if B + m >= 60:
    h += 1

print(f'{(A + h) % 24} {(B + m) % 60}')
