# 벌집

N = int(input())

n = 1
i = 0
while True:
    n += 6 * i
    i += 1
    if N <= n:
        print(i)
        break
