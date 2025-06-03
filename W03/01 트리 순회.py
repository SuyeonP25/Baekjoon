# 트리 순회

import sys

N = int(sys.stdin.readline())
T = dict()
for _ in range(N):
    p, l, r = sys.stdin.readline().split()
    T[p] = (l, r)


def treetraverse(p, mod):
    if mod == 'pre':
        print(p, end='')
        treetraverse(T[p][0], mod) if T[p][0] != '.' else print('', end='')
        treetraverse(T[p][1], mod) if T[p][1] != '.' else print('', end='')
    elif mod == 'in':
        treetraverse(T[p][0], mod) if T[p][0] != '.' else print('', end='')
        print(p, end='')
        treetraverse(T[p][1], mod) if T[p][1] != '.' else print('', end='')
    elif mod == 'post':
        treetraverse(T[p][0], mod) if T[p][0] != '.' else print('', end='')
        treetraverse(T[p][1], mod) if T[p][1] != '.' else print('', end='')
        print(p, end='')


treetraverse('A', 'pre')
print()
treetraverse('A', 'in')
print()
treetraverse('A', 'post')
print()
