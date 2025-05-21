# 배스킨라빈스 31

N = int(input())
l = []
for i in range(N):
    l.append(list(map(int, input().split())))

maxGameCnt = 10000
maxGameN = 0
for i in range(N):
    games = 2 + (l[i][0] - 1) // (l[i][1] + 1) * 2
    if games < maxGameCnt:
        maxGameCnt = games
        maxGameN = i + 1

print(f'{maxGameN} {maxGameCnt}')
