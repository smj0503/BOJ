# BOJ 9465 '스티커'

import sys
input = sys.stdin.readline

T = int(input())
N = int(input())

sticker = []
for _ in range(2):
    sticker.append([0] + list(map(int, input().split())))

dp = [0] * (N + 1)

dp[1] = max(sticker[0][1], sticker[1][1])
dp[2] = max(sticker[0][1] + sticker[1][2], sticker[1][1] + sticker[0][2])
print(dp)
