# 백준 12852 '1로 만들기 2'

import sys
input = sys.stdin.readline

N = int(input())
pre = [0, 0]
dp = [0, 0]

for i in range(2, N + 1):
    dp.append(dp[i - 1] + 1)
    pre.append(i - 1)
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        pre[i] = i // 2
    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        pre[i] = i // 3

print(dp[N])
cur = N
while True:
    print(cur, end=' ')
    if cur == 1: break
    cur = pre[cur]
