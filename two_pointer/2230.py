# 백준 2230 '수 고르기'

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

gap = 10 ** 10
en = 0

for st in range(N):
    while en < N and arr[en] - arr[st] < M:
        en += 1
    if en == N:
        break
    gap = min(gap, arr[en] - arr[st])

print(gap)
