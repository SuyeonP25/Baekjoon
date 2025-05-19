import itertools

N = int(input())
l = list(map(int, input().split()))

p = itertools.permutations(l)
maxsum = [0]

for i in p:
    sum = 0
    for j in range(N - 1):
        sum += abs(i[j] - i[j + 1])
    if sum > maxsum[0]:
        maxsum[0] = sum

print(maxsum[0])
