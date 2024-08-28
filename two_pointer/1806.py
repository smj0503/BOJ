# 백준 1806 '부분합'

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

gap = 10 ** 10
en = 0
total = arr[0]

for st in range(N):
    while en < N and total < S:
        en += 1
        if en != N:
            total += arr[en]
    if en == N:
        break
    gap = min(gap, en - st + 1)
    total -= arr[st]

if gap == 10 ** 10:
    gap = 0

print(gap)
