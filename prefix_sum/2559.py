# BOJ 2559 '수열'

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0]
temp = 0

for a in arr:
    temp += a
    prefix_sum.append(temp)

res = []
for i in range(N-K+1):
    res.append(prefix_sum[i+K] - prefix_sum[i])

print(max(res))
