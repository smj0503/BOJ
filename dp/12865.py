# 백준 12865 '평범한 배낭'
# DP[i][j] : i개의 물건이 있고, 무게 j만큼 배낭을 채울 수 있을 때, 가져갈 수 있는 물건들의 가치의 최대값
# DP[i][j]의 정의에 따르면 점화식은 다음과 같이 설계할 수 있다.
# DP[i][j] = max(DP[i-1][j], DP[i-1][j-w[i]] + v[i]), (w[i] <= j)

# 물건을 배낭에 담을 때,
# ① "현재 배낭의 허용 무게" < "넣을 물건의 무게" 이면 (현재)물건을 넣지 않는다.
# ② 그렇지 않다면, 다음 중 더 나은 가치를 선택해 넣는다
# 2-1) 현재 넣을 물건의 무게 만큼 배낭에서 뺀다. 그리고 현재 물건을 넣는다. (물건을 넣었으니까, 그 무게 만큼 배낭의 용량에서 빼 준다.)
# 2-2) 현재 물건을 넣지 않고 이전 배낭 그대로 가지고 간다.

# 현재 담을 물건의 인덱스를 i, 현재 가방 허용 용량이 j, 현재 담을 물건의 무게는 weight, 가치는 value 일 때,
# ① j < weight : d[i][j] = d[i-1][j]
# ② d[i][j] = max(d[i-1][j-weight] + value, d[i-1][j])
# 2-1) d[i-1][j-weight] + value
# 2-2) d[i-1][j]

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [[0, 0]]
for _ in range(N):
    w, v = map(int, input().split())
    items.append([w, v])
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    w, v = items[i]
    for j in range(1, K+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])

print(dp[N][K])
