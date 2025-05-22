# 더하기 사이클

N = int(input())

cycle = 1
newN = N % 10 * 10 + (N // 10 + N % 10) % 10

while N != newN:
    cycle += 1
    newN = newN % 10 * 10 + (newN // 10 + newN % 10) % 10

print(cycle)
