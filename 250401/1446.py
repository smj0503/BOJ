# BOJ 1446 '지름길'

# dp 풀이
# 최단 거리 테이블 생성(dp) -> [0, 1, 2, 3, ..., D]
# dp[i] = min(dp[i], dp[i-1] + 1)

N, D = map(int, input().split())
short_cuts = [list(map(int, input().split())) for _ in range(N)]
dp = [i for i in range(D + 1)]

for i in range(D + 1):
    dp[i] = min(dp[i], dp[i - 1] + 1)

    for st, en, d in short_cuts:
        if i == st and en <= D:
            dp[en] = min(dp[en], dp[st] + d)

print(dp[D])
