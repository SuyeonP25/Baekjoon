# 공 넣기

N, M = map(int, input().split())
l = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for a in range(i - 1, j):
        l[a] = k

for i in range(N):
    print(f'{l[i]}', end=' ')
