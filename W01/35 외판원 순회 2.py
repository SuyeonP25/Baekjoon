N = int(input())
D = []
for i in range(N):
    D.append(list(map(int, input().split())))

INF = 999999999
dp = [[INF] * 2 ** N for i in range(N)]
dp[0][1] = 0

for A in range(2 ** N):
    for last_check in range(N):
        if not (A & (2 ** last_check)):
            continue
        for next_check in range(N):
            if A & (2 ** next_check):
                continue
            if D[last_check][next_check] == 0:
                continue
            nextA = A | (2 ** next_check)
            dp[next_check][nextA] = min(dp[next_check][nextA], dp[last_check][A] + D[last_check][next_check])

min_dist = INF
for i in range(1, N):
    if D[i][0] != 0:
        min_dist = min(min_dist, dp[i][2 ** N - 1] + D[i][0])
print(min_dist)
