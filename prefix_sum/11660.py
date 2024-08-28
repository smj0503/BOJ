# BOJ 11659 '구간 합 구하기 5'

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
prefix_sum = [[0] * (N + 1)]

for _ in range(N):
    prefix_sum.append([0] + list(map(int, input().split())))

# 누적합 배열(prefix_sum) 값 채우기
# 1. 행 별로 더하기
for i in range(1, N + 1):
    for j in range(1, N):
        prefix_sum[i][j + 1] += prefix_sum[i][j]

# 2. 열 별로 더하기
for j in range(1, N + 1):
    for i in range(1, N):
        prefix_sum[i + 1][j] += prefix_sum[i][j]

# (x1, y1)에서 (x2, y2)까지의 합
# prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1])
