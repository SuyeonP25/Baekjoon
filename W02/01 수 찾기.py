# 수 찾기

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
Mlist = list(map(int, input().split()))

for m in Mlist:
    pl, pr = 0, N-1
    while True:
        center = (pl+pr)//2
        if A[center] == m:
            print(1)
            break
        elif A[center] < m:
            pl = center+1
        else:
            pr = center -1
        if pl>pr:
            print(0)
            break