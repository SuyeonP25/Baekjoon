# 동전

import sys

T = int(sys.stdin.readline())

# L 안에 M 보다 큰 수가 없음을 가정하는 풀이
# 만약 위를 보장하는 조건이 없을시 DP[i][0] = 1 을 사용하는 풀이는 불가
# L[i]가 M보다 작은 경우에만 DP[i][L[i]에만 1을 더해주는 식을 반복문 내에 추가

for _ in range(T):
    N = int(sys.stdin.readline())
    L = [0] + list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    DP = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        DP[i][0] = 1

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            DP[i][j] = DP[i - 1][j]
            if j >= L[i]:
                DP[i][j] += DP[i][j - L[i]]

    print(DP[N][M])
