w, h = map(int, input().split())
n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
wcut = []
hcut = []
for i in range(n):
    if l[i][0]==0:
        hcut.append(l[i][1])
    else:
        wcut.append(l[i][1])
wcut.sort(reverse=True)
hcut.sort(reverse=True)
wcuts = []
hcuts = []
for i in range(len(wcut)):
    wcuts.append(w-wcut[i])
    w = wcut[i]
wcuts.append(w)
for i in range(len(hcut)):
    hcuts.append(h-hcut[i])
    h = hcut[i]
hcuts.append(h)
print(max(wcuts)*max(hcuts))