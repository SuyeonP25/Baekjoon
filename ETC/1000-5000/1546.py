# 평균

N = int(input())
l = list(map(int, input().split()))

print(sum(l) / N / max(l) * 100)
