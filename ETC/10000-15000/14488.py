# 준오는 급식충이야!!

N, T = map(float, input().split())
N = int(N)
x = list(map(int, input().split()))
v = list(map(int, input().split()))
isPossible = True

pl = round(x[0] - T * v[0], 4)
pr = round(x[0] + T * v[0], 4)

for i in range(1, N):
    xl = round(x[i] - T * v[i], 4)
    xr = round(x[i] + T * v[i], 4)
    
    if xr < pl:
        isPossible = False
        break
    if xl > pr:
        isPossible = False
        break
    if xr < pr:
        pr = xr
    if xl > pl:
        pl = xl

if isPossible:
    print(1)
else:
    print(0)
