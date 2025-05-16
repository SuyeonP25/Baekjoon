N, X = map(int, input().split())
l = input().split()

for i in range(N):
    if int(l[i]) < X:
        print(l[i], end=' ')