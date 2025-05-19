N = int(input())
s = set()
for i in range(N):
    s.add(input())
l = sorted(s, key=lambda x: (len(x), x))
for i in l:
    print(i)
