# 공 바꾸기

N, M = map(int, input().split())
l = []
for i in range(1, N + 1):
    l.append(i)

for _ in range(M):
    i, j = map(int, input().split())
    l[i - 1], l[j - 1] = l[j - 1], l[i - 1]

for i in range(N):
    print(f'{l[i]}', end=' ')
