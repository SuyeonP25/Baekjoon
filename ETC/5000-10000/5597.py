# 과제 안 내신 분..?

l = []

for i in range(1, 31):
    l.append(i)

for _ in range(28):
    s = int(input())
    l.remove(s)

l = sorted(l)
print(l[0])
print(l[1])
