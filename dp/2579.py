# 백준 2579번 '계단 오르기'

import sys
input = sys.stdin.readline

N = int(input())
stair = [0]
for _ in range(N):
    stair.append(int(input()))

dp = [0] * (N + 1)

if N <= 2:
    print(sum(stair))
else:
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]

    for i in range(3, N + 1):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])
    print(dp[-1])

