# 분해합

N = int(input())
if N < 60:
    for n in range(N):
        if n + sum(int(c) for c in str(n)) == N:
            print(n)
            exit()
else:   # 큰 수의 경우 반복 횟수 줄이기
    for n in range(N - 60, N):
        if n + sum(int(c) for c in str(n)) == N:
            print(n)
            exit()

print(0)
