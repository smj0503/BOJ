# 백준 11659 '구간 합 구하기 4'

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
ranges = []

for _ in range(M):
    i, j = map(int, input().split())
    ranges.append([i, j])

dp = [0]
for i in range(1, N + 1):
    dp.append(dp[i - 1] + numbers[i-1])

for r in ranges:
    print(dp[r[1]] - dp[r[0] - 1])
