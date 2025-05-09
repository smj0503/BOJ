# BOJ 2839 '설탕 배달'

INF = int(1e9)

n = int(input())
dp = [INF for _ in range(5001)]

dp[3] = 1
dp[5] = 1

for i in range(6, n+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1

if dp[n] >= INF:
    print(-1)
else:
    print(dp[n])
