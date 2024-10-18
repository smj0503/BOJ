# BOJ 11660 '구간합 구하기 5'

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[0] * (N+1)]

for _ in range(N):
    dp.append([0] + list(map(int, input().split())))

for i in range(N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i][j] + dp[i][j-1]

for i in range(N+1):
    for j in range(1, N+1):
        dp[j][i] = dp[j][i] + dp[j-1][i]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])
