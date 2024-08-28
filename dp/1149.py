# 백준 1149 'RGB 거리'

import sys
input = sys.stdin.readline

N = int(input())
red = [0]
green = [0]
blue = [0]

# red, blue, green 배열 세팅
for _ in range(N):
    r, g, b = map(int, input().split())
    red.append(r)
    green.append(g)
    blue.append(b)

# dp 배열 세팅
dp = [0] + [[0 for _ in range(3)] for _ in range(N)]

# 초기값 설정
dp[1][0] = red[1]
dp[1][1] = green[1]
dp[1][2] = blue[1]

for i in range(2, N + 1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + red[i]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + green[i]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + blue[i]

result = min(dp[N])
print(result)
