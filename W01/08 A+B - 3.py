T = int(input())
l = []

for i in range(T):
    l = l + list(map(int, input().split()))

for i in range(T):
    print(l[2*i] + l[2*i+1])