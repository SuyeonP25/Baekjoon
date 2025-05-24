# 부녀회장이 될테야

l = list()
l.append(list(i for i in range(15)))
for _ in range(14):
    l.append(list(0 for _ in range(15)))

for i in range(1,15):
    for j in range(15):
        l[i][j] = sum(l[i-1][0:j+1])

T=int(input())
for _ in range(T):
    k,n = int(input()),int(input())
    print(l[k][n])
