# 영수증

X, N = int(input()), int(input())
total = 0

for i in range(N):
    a, b = map(int, input().split())
    total += a * b

if total == X:
    print("Yes")
else:
    print("No")
