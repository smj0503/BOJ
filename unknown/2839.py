# BOJ 2839 '설탕 배달'

N = int(input())
dp = [-1] * 5001
dp[3] = 1
dp[5] = 1

if N <= 5:
    print(dp[N])
else:
    for i in range(6, N + 1):
        # i = 홀수
        if i % 2 == 1:
            for j in range(1, (i + 1) // 2):
                if dp[j] != -1 and dp[i - j] != -1:
                    count = dp[j] + dp[i - j]
                    if dp[i] > 0:
                        dp[i] = min(count, dp[i])
                    else:
                        dp[i] = count
        # i = 짝수
        else:
            for j in range(1, (i + 1) // 2 + 1):
                if dp[j] != -1 and dp[i - j] != -1:
                    count = dp[j] + dp[i - j]
                    if dp[i] > 0:
                        dp[i] = min(count, dp[i])
                    else:
                        dp[i] = count
    print(dp[N])
