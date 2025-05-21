# 바구니 뒤집기

N, M = map(int, input().split())
l = list()
for i in range(N):
    l.append(i + 1)

for _ in range(M):
    i, j = map(int, input().split())
    for a in range((j - i) // 2 + 1):
        l[i - 1 + a], l[j - 1 - a] = l[j - 1 - a], l[i - 1 + a]

for a in l:
    print(a, end=' ')
