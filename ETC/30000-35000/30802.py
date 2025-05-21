# 웰컴 키트

N = int(input())
TS = list(map(int, input().split()))
T, P = map(int, input().split())

tsum = 0
for i in range(len(TS)):
    tsum += TS[i] // T
    if TS[i] % T != 0:
        tsum += 1
print(tsum)
print(N // P, N % P)
