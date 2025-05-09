# BOJ 1149 'RGB 거리'
# DP[i][j] : i번째 집을 j번째 색으로 칠하는 최소 비용

import sys
input = sys.stdin.readline

n = int(input())
colors = [list(map(int, input().split())) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n)]

dp[0][0] = colors[0][0]
dp[0][1] = colors[0][1]
dp[0][2] = colors[0][2]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + colors[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + colors[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + colors[i][2]

print(min(dp[n-1]))
