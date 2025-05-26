# 색종이 만들기

# import sys
#
# N = int(sys.stdin.readline())
# L = list()
# for _ in range(N):
#     L.append(list(map(int, sys.stdin.readline().split())))
#
# B, W = 0, 0
#
# def cut_check(i, j, n):
#     global B
#     global W
#
#     if n == 1:
#         if L[i][j] == 1:
#             B += 1
#         if L[i][j] == 0:
#             W += 1
#     else:
#         # ul
#         sum = 0
#         for a in range(i, i + n // 2):
#             for b in range(j, j + n // 2):
#                 sum += L[a][b]
#         if sum == 0:
#             W += 1
#         elif sum == (n // 2) ** 2:
#             B += 1
#         else:
#             cut_check(i, j, n // 2)
#
#         # ur
#         sum = 0
#         for a in range(i + n // 2, i + n):
#             for b in range(j, j + n // 2):
#                 sum += L[a][b]
#         if sum == 0:
#             W += 1
#         elif sum == (n // 2) ** 2:
#             B += 1
#         else:
#             cut_check(i + n // 2, j, n // 2)
#
#         # dl
#         sum = 0
#         for a in range(i, i + n // 2):
#             for b in range(j + n // 2, j + n):
#                 sum += L[a][b]
#         if sum == 0:
#             W += 1
#         elif sum == (n // 2) ** 2:
#             B += 1
#         else:
#             cut_check(i, j + n // 2, n // 2)
#
#         # dr
#         sum = 0
#         for a in range(i + n // 2, i + n):
#             for b in range(j + n // 2, j + n):
#                 sum += L[a][b]
#         if sum == 0:
#             W += 1
#         elif sum == (n // 2) ** 2:
#             B += 1
#         else:
#             cut_check(i + n // 2, j + n // 2, n // 2)
#
# sum=0
# for i in range(N):
#     for j in range(N):
#         sum += L[i][j]
# if sum == 0:
#     print(1)
#     print(0)
# elif sum == N**2:
#     print(0)
#     print(1)
# else:
#     cut_check(0, 0, N)
#
#     print(W)
#     print(B)

import sys

N = int(sys.stdin.readline())
L = list()
for _ in range(N):
    L.append(list(map(int, sys.stdin.readline().split())))

B, W = 0, 0


def check(i, j, n):
    global B
    global W

    standard = L[i][j]
    cut_needed = False
    for k in range(n):
        for l in range(n):
            if L[i + k][j + l] != standard:
                cut_needed = True
                break

    if not cut_needed:
        if standard:
            B += 1
        else:
            W += 1
    else:
        check(i, j, n // 2)
        check(i + n // 2, j, n // 2)
        check(i, j + n // 2, n // 2)
        check(i + n // 2, j + n // 2, n // 2)


check(0, 0, N)
print(W)
print(B)
