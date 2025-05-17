# counting sort modified
N = int(input())
l = [0] * 10001

for i in range(N):
    a = int(input())
    l[a] += 1

for i in range(10001):
    for j in range(l[i]):
        print(i)