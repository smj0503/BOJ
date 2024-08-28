# 백준 11726 '2xn 타일링'

import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1, 2]
mod = 10007

for i in range(3, n + 1):
    dp.append((dp[i-1] + dp[i-2]) % mod)

print(dp[n])
