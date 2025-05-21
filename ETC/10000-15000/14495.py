# 피보나치 비스무리한 수열

N = int(input())

l = [1, 1, 1]

if N > 3:
    for i in range(3, N):
        l.append(l[i - 1] + l[i - 3])

print(l[N - 1])
