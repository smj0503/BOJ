# 백준 2217 '로프'

import sys
input = sys.stdin.readline

N = int(input())
weights = [int(input()) for _ in range(N)]
weights.sort()

max_weight = 0
for k in range(1, N + 1):
    max_weight = max(max_weight, weights[N - k] * k)

print(max_weight)
