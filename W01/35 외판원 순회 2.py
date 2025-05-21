import math
import itertools

N = int(input())
l = []
city = []
for i in range(N):
    l.append(list(map(int, input().split())))
    city.append(i)
city.remove(0)

mindist = math.inf
cityP = itertools.permutations(city)

for p in cityP:
    dist = 0
    valid = True

    if l[0][p[0]] == 0:
        continue
    else:
        dist += l[0][p[0]]

    for i in range(N - 2):
        if l[p[i]][p[i + 1]] == 0:
            valid = False
            break
        else:
            dist += l[p[i]][p[i + 1]]

    if not valid or l[p[N - 2]][0] == 0:
        continue
    else:
        dist += l[p[N - 2]][0]

    if dist < mindist:
        mindist = dist

print(mindist)
