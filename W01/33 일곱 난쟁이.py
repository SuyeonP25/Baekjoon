d = 9
l = [0] * d

for i in range(d):
    l[i] = int(input())
l.sort()
total = sum(l)

ans1, ans2 = 0, 0
ansFound = False
for i in range(d):
    for j in range(d):
        if l[i] + l[j] == total - 100 and i != j:
            ans1, ans2 = i, j
            ansFound = True
            break
    if ansFound:
        break

for i in range(d):
    if i != ans1 and i != ans2:
        print(l[i])
