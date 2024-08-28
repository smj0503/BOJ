# BOJ 2851 '슈퍼 마리오'

import sys
input = sys.stdin.readline

score = []
for _ in range(10):
    score.append(int(input()))

prefix_sum = []
temp = 0

for s in score:
    temp += s
    prefix_sum.append(temp)

idx = 0
for i in range(1, 10):
    if abs(prefix_sum[i] - 100) <= abs(prefix_sum[i-1] - 100):
        idx = i

print(prefix_sum[idx])
